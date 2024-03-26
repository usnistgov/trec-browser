# Proceedings - Blog 2007 

#### Overview of the TREC 2007 Blog Track

_Craig Macdonald, Iadh Ounis, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/BLOG.OVERVIEW16.pdf](http://trec.nist.gov/pubs/trec16/papers/BLOG.OVERVIEW16.pdf)
??? abstract "Abstract"
	
	The goal of the Blog track is to explore the information seeking behaviour in the blogosphere. It aims to create the required infrastructure to facilitate research into the blogosphere and to study retrieval from blogs and other related applied tasks. The track was introduced in 2006 with a main opinion finding task and an open task, which allowed participants the opportunity to influence the determination of a suitable second task for 2007 on other aspects of blogs besides their opinionated nature. As a result, we have created the first blog test collection, namely the TREC Blog06 collection, for adhoc retrieval and opinion finding. Further background information on the Blog track can be found in the 2006 track overview [2]. TREC 2007 has continued using the Blog06 collection, and saw the addition of a new main task and a new subtask, namely a blog distillation (feed search) task and an opinion polarity subtask respectively, along with a second year of the opinion finding task. NIST developed the topics and relevance judgments for the opinion finding task, and its polarity subtask. For the blog distillation task, the participating groups created the topics and the associated relevance judgments. This second year of the track has seen an increased participation compared to 2006, with 20 groups submitting runs to the opinion finding task, 11 groups submitting runs to the polarity subtask, and 9 groups submitting runs to the blog distillation task. This paper provides an overview of each task, summarises the obtained results and draws conclusions for the future. The remainder of this paper is structured as follows. Section 2 provides a short description of the used Blog06 collection. Section 3 describes the opinion finding task and its polarity subtask, providing an overview of the submitted runs, as well as a summary of the main used techniques by the participants. Section 4 describes the newly created blog distillation (feed search) task, and summarises the results of the runs and the main approaches deployed by the participating groups. We provide concluding remarks in Section 5.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MacdonaldOS07.bib) "
	```
	@inproceedings{DBLP:conf/trec/MacdonaldOS07,
		author = {Craig Macdonald and Iadh Ounis and Ian Soboroff},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Overview of the {TREC} 2007 Blog Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/BLOG.OVERVIEW16.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MacdonaldOS07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FUB, IASI-CNR and University of Tor Vergata at TREC 2007 Blog  Track

_Gianni Amati, Edgardo Ambrosi, Marco Bianchi, Carlo Gaibisso, Giorgio Gambosi_

- :fontawesome-solid-user-group: **Participant:** [fondazione-ug-bordoni-netlab-team](./participants.md#fondazione-ug-bordoni-netlab-team)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/fub.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/fub.blog.final.pdf)
- :material-file-search: **Runs:** [FIUbPL2](./runs.md#fiubpl2) | [FIUdPL2](./runs.md#fiudpl2) | [FIUlPL2](./runs.md#fiulpl2) | [FIUlP22](./runs.md#fiulp22) | [FIUlDPH](./runs.md#fiuldph) | [FIUDDPH](./runs.md#fiuddph)

??? abstract "Abstract"
	
	We present a fully automatic and weighted dictionary to be used in topical opinion retrieval. We also define a simple topical opinion retrieval function that is free from parameters, so that the retrieval does not need any learning or tuning phase.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AmatiABGG07.bib) "
	```
	@inproceedings{DBLP:conf/trec/AmatiABGG07,
		author = {Gianni Amati and Edgardo Ambrosi and Marco Bianchi and Carlo Gaibisso and Giorgio Gambosi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {FUB, {IASI-CNR} and University of Tor Vergata at {TREC} 2007 Blog Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/fub.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AmatiABGG07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Opinion Retrieval Experiments Using Generative Models: Experiments  for the TREC 2007 Blog Track

_Yuki Arai, Koji Eguchi_

- :fontawesome-solid-user-group: **Participant:** [kobeu.eguchi](./participants.md#kobeu.eguchi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/nii.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/nii.blog.final.pdf)
- :material-file-search: **Runs:** [KobePrMIR01](./runs.md#kobeprmir01) | [KobePrMIR02](./runs.md#kobeprmir02) | [KobePrMIR03](./runs.md#kobeprmir03) | [KobePrMIR04](./runs.md#kobeprmir04) | [KobePrMIR05](./runs.md#kobeprmir05) | [KobePrMIR06](./runs.md#kobeprmir06)

??? abstract "Abstract"
	
	Ranking blog posts that express opinions regarding a given topic should serve a critical function in helping users. We explored a couple of methods for opinion retrieval in the framework of probabilistic language models. The first method combines topic-relevance model and opinion-relevance model, at document level, that captures topic dependence of the opinion expressions. The second method combines the aforementioned topic-opinion relevance models at sentence level, and accumulates the negative cross entropy between the combined relevance models and each sentence model to obtain a document-level score. This paper reports the overview of our methods and the evaluation results on the Opinion Retrieval Task at the TREC 2007 Blog Track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AraiE07.bib) "
	```
	@inproceedings{DBLP:conf/trec/AraiE07,
		author = {Yuki Arai and Koji Eguchi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Opinion Retrieval Experiments Using Generative Models: Experiments for the {TREC} 2007 Blog Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/nii.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AraiE07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Texas School of Information at TREC 2007

_Miles Efron, Don Turnbull, Carlos Ovalle_

- :fontawesome-solid-user-group: **Participant:** [utexas-austin.efron](./participants.md#utexas-austin.efron)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/utexas-austin.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/utexas-austin.blog.final.pdf)
- :material-file-search: **Runs:** [utlc](./runs.md#utlc) | [utplmu100](./runs.md#utplmu100) | [utblnrr](./runs.md#utblnrr) | [utblrr](./runs.md#utblrr)

??? abstract "Abstract"
	
	This was the first year in which the University of Texas' School of Information (UT iSchool) participated in TREC. We limited our attention to a single task (feed distillation) within a single track (Blog). Our goal was to obtain high-precision results within a principled theoretical framework. Our system used Apache's Lucene library [1] for its core indexing and retrieval functions. We also relied on language modeling extensions to Lucene provided by the Informatics Institute at the University of Amsterdam [2]. However, We altered these libraries to enable our IR approach. In particular, our results rely on a variant of the Kullback-Leibler (KL) divergence model [3, 4]. Given a query q we derive a score for each feed f in the corpus by the negative KL-divergence between the query language model and the language model for f. In the interest of maximizing precision at low numbers of documents retrieved, we limited our analysis to each feed's RSS posts, as opposed to its complete HTML representation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EfronTO07.bib) "
	```
	@inproceedings{DBLP:conf/trec/EfronTO07,
		author = {Miles Efron and Don Turnbull and Carlos Ovalle},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Texas School of Information at {TREC} 2007},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/utexas-austin.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EfronTO07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Retrieval and Feedback Models for Blog Distillation

_Jonathan L. Elsas, Jaime Arguello, Jamie Callan, Jaime G. Carbonell_

- :fontawesome-solid-user-group: **Participant:** [cmu.dir.callan](./participants.md#cmu.dir.callan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/cmu-callan.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/cmu-callan.blog.final.pdf)
- :material-file-search: **Runs:** [CMUfeed](./runs.md#cmufeed) | [CMUfeedW](./runs.md#cmufeedw) | [CMUentry](./runs.md#cmuentry) | [CMUentryW](./runs.md#cmuentryw)

??? abstract "Abstract"
	
	This paper presents our system and results for the Feed Distillation task in the Blog track at TREC 2007. Our experiments focus on two dimensions of the task: (1) a large-document model (feed retrieval) vs. a small-document model (entry or post retrieval) and (2) a novel query expansion method using the link structure and link text found within Wikipedia.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ElsasACC07.bib) "
	```
	@inproceedings{DBLP:conf/trec/ElsasACC07,
		author = {Jonathan L. Elsas and Jaime Arguello and Jamie Callan and Jaime G. Carbonell},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Retrieval and Feedback Models for Blog Distillation},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/cmu-callan.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ElsasACC07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Language Modeling Approaches to Blog Postand Feed Finding

_Breyten Ernsting, Wouter Weerkamp, Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [uamsterdam.deRijke](./participants.md#uamsterdam.derijke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uamsterdam-weerkamp.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uamsterdam-weerkamp.blog.final.pdf)
- :material-file-search: **Runs:** [uams07indbl](./runs.md#uams07indbl) | [uams07topic](./runs.md#uams07topic) | [uams07mmbl](./runs.md#uams07mmbl) | [uams07mmq](./runs.md#uams07mmq) | [uams07mmqop](./runs.md#uams07mmqop) | [uams07mmqcom](./runs.md#uams07mmqcom) | [uams07polqop](./runs.md#uams07polqop) | [uams07polqco](./runs.md#uams07polqco) | [uams07polq](./runs.md#uams07polq) | [uams07polbl](./runs.md#uams07polbl) | [uams07ipolt](./runs.md#uams07ipolt) | [uams07bdtop](./runs.md#uams07bdtop) | [uams07bdfreq](./runs.md#uams07bdfreq) | [uams07bdtblm](./runs.md#uams07bdtblm)

??? abstract "Abstract"
	
	We describe our participation in the TREC 2007 Blog track. In the opinion task we looked at the differences in performance between Indri and our mixture model, the influence of external expansion and document priors to improve opinion finding; results show that an out-of-the-box Indri implementation outperforms our mixture model, and that external expansion on a news corpus is very benificial. Opinion finding can be improved using either lexicons or the number of comments as document priors. Our approach to the feed distillation task is based on aggregating post-level scores to obtain a feed-level ranking. We integrated time-based and persistence aspects into the retrieval model. After correcting bugs in our post-score aggregation module we found that time-based retrieval improves results only marginally, while persistence-based ranking results in substantial improvements under the right circumstances.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ErnstingWR07.bib) "
	```
	@inproceedings{DBLP:conf/trec/ErnstingWR07,
		author = {Breyten Ernsting and Wouter Weerkamp and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Language Modeling Approaches to Blog Postand Feed Finding},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uamsterdam-weerkamp.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ErnstingWR07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IR-Specific Searches at TREC 2007: Genomics & Blog Experiments

_Claire Fautsch, Jacques Savoy_

- :fontawesome-solid-user-group: **Participant:** [uneuchatel.savoy](./participants.md#uneuchatel.savoy)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uneuchatel.geo.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uneuchatel.geo.blog.final.pdf)
- :material-file-search: **Runs:** [UniNEblog1](./runs.md#unineblog1) | [UniNEblog2](./runs.md#unineblog2) | [UniNEblog3](./runs.md#unineblog3) | [UniNEblog4](./runs.md#unineblog4) | [UniNEblog5](./runs.md#unineblog5) | [UniNEblog6](./runs.md#unineblog6)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC 2007 Genomics and Blog evaluation campaigns. Within these two tracks, our main intent is to go beyond simple document retrieval, using different search and filtering strategies to obtain more specific answers to user information needs. In the Genomics track, the dedicated IR system has to extract relevant text passages in support of precise user questions. This task may also be viewed as the first stage of a Question/Answering system. In the Blog track we explore various strategies for retrieving opinions from the blogsphere, which in this case involves subjective opinions about various targets entities (e.g., person, location, organization, event, product or technology). This task can be subdivided in two parts: 1) retrieve relevant information (facts) and 2) extract positive, negative or mixed opinions about the specific entity being targeted. To achieve these objectives we evaluate retrieval effectiveness using the Okapi (BM25) and various other models derived from the Divergence from Randomness (DFR) paradigm, as well as a language model (LM). Through our experiments with the Genomics corpus we find that the DFR models perform clearly better than the Okapi model (relative difference of 70%) in terms of mean average precision (MAP). Using the blog corpus, we found the opposite; the Okapi model performs slightly better than both DFR models (relative difference around 5%) and LM (relative difference 7%) model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FautschS07.bib) "
	```
	@inproceedings{DBLP:conf/trec/FautschS07,
		author = {Claire Fautsch and Jacques Savoy},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {IR-Specific Searches at {TREC} 2007: Genomics {\&} Blog Experiments},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uneuchatel.geo.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FautschS07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2007: Experiments in Blog and Enterprise  Tracks with Terrier

_David Hannah, Craig Macdonald, Jie Peng, Ben He, Iadh Ounis_

- :fontawesome-solid-user-group: **Participant:** [glasgow.ounis](./participants.md#glasgow.ounis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uglasgow.blog.ent.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uglasgow.blog.ent.final.pdf)
- :material-file-search: **Runs:** [uogBOPF](./runs.md#uogbopf) | [uogBOPFTDW](./runs.md#uogbopftdw) | [uogBOPFProxW](./runs.md#uogbopfproxw) | [uogBOPFTD](./runs.md#uogbopftd) | [uogBOPFProx](./runs.md#uogbopfprox) | [uogBOPFPol](./runs.md#uogbopfpol) | [uogBOPFTDOF](./runs.md#uogbopftdof) | [uogBDFeMNZ](./runs.md#uogbdfemnz) | [uogBDFeMNZP](./runs.md#uogbdfemnzp) | [uogBDFeMNZpC](./runs.md#uogbdfemnzpc) | [uogBDFeMNZhA](./runs.md#uogbdfemnzha)

??? abstract "Abstract"
	
	In TREC 2007, we participate in four tasks of the Blog and Enterprise tracks. We continue experiments using Terrier1 [14], our modular and scalable Information Retrieval (IR) platform, and the Divergence From Randomness (DFR) framework. In particular, for the Blog track opinion finding task, we propose a statistical term weighting approach to identify opinionated documents. An alternative approach based on an opinion identification tool is also utilised. Overall, a 15% improvement over a non-opinionated baseline is observed in applying the statistical term weighting approach. In the Expert Search task of the Enterprise track, we investigate the use of proximity between query terms and candidate name occurrences in documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HannahMPHO07.bib) "
	```
	@inproceedings{DBLP:conf/trec/HannahMPHO07,
		author = {David Hannah and Craig Macdonald and Jie Peng and Ben He and Iadh Ounis},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {University of Glasgow at {TREC} 2007: Experiments in Blog and Enterprise Tracks with Terrier},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uglasgow.blog.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HannahMPHO07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Feed Distillation Using AdaBoost and Topic Maps

_Wai-Lung Lee, Andreas Lommatzsch, Christian Scheel_

- :fontawesome-solid-user-group: **Participant:** [uberlin.neubauer](./participants.md#uberlin.neubauer)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/techu-berlin.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/techu-berlin.blog.final.pdf)
- :material-file-search: **Runs:** [ADABoostM1](./runs.md#adaboostm1)

??? abstract "Abstract"
	
	This paper retains the experiences by participating in TREC 2007 Blog Track 'Feed Distillation'. To perform the run various classifiers are combined, which analyze title-, content- and splog-specific features to predict the relevance of a feed related to a topic, based on the idea of AdaBoost. The implemented classifiers utilize keywords retrieved from different thesauri such as Wordnet and Wortschatz, as well as from websites providing hierarchical organized 'ontol ogy' such as the 'Open Directory Project' and Yahoo Directory. To structure the keywords, Topic Maps are utilized according to ISO/IEC 13250:2000.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LeeLS07.bib) "
	```
	@inproceedings{DBLP:conf/trec/LeeLS07,
		author = {Wai{-}Lung Lee and Andreas Lommatzsch and Christian Scheel},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Feed Distillation Using AdaBoost and Topic Maps},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/techu-berlin.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LeeLS07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments in TREC 2007 Blog Opinion Task at CAS-ICT

_Xiangwen Liao, Donglin Cao, Yu Wang, Wei Liu, Songbo Tan, Hongbo Xu, Xueqi Cheng_

- :fontawesome-solid-user-group: **Participant:** [cas-liu](./participants.md#cas-liu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/cas-ict.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/cas-ict.blog.final.pdf)
- :material-file-search: **Runs:** [Relevant](./runs.md#relevant) | [DrapCom](./runs.md#drapcom) | [DrapOpi](./runs.md#drapopi) | [DrapStm](./runs.md#drapstm) | [BaseSmp](./runs.md#basesmp) | [SmpStm](./runs.md#smpstm) | [DrapComSub](./runs.md#drapcomsub) | [DrapOpiSub](./runs.md#drapopisub) | [DrapStmSub](./runs.md#drapstmsub)

??? abstract "Abstract"
	
	This paper describes our participation in TREC 2007 Blog Track Tasks: Opinion retrieval and Polarity classification. As for Opinion retrieval task, a two-step approach is used to retrieve opinion relevant blog unit (that is blog post and its comments) given a query after filtering Spam blog and extracting blog unit. With Polarity Classification, Drag-push [1] based classifier is employed to get polarity of blog unit. Finally, we introduce all the runs submitted.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiaoCWLTXC07.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiaoCWLTXC07,
		author = {Xiangwen Liao and Donglin Cao and Yu Wang and Wei Liu and Songbo Tan and Hongbo Xu and Xueqi Cheng},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments in {TREC} 2007 Blog Opinion Task at {CAS-ICT}},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/cas-ict.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiaoCWLTXC07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NTU at TREC 2007 Blog Track

_Kevin Hsin-Yih Lin, Hsin-Hsi Chen_

- :fontawesome-solid-user-group: **Participant:** [ntu.chen](./participants.md#ntu.chen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/ntu.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/ntu.blog.final.pdf)
- :material-file-search: **Runs:** [NTUAuto](./runs.md#ntuauto) | [NTUAutoOp](./runs.md#ntuautoop) | [NTUManual](./runs.md#ntumanual) | [NTUManualOp](./runs.md#ntumanualop) | [NTUManualOpP](./runs.md#ntumanualopp) | [NTUAutoOpP](./runs.md#ntuautoopp)

??? abstract "Abstract"
	
	We participated in the Opinion Retrieval Task and the Polarity Subtask. An SVM classifier was used to determine the opinion polarities of documents. We found that the opinion mean average precisions for the runs using the SVM classifier is better than the opinion mean average precisions for the runs produced solely by the TFIDF retrieval model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinC07.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinC07,
		author = {Kevin Hsin{-}Yih Lin and Hsin{-}Hsi Chen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{NTU} at {TREC} 2007 Blog Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/ntu.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LinC07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NLPR in TREC 2007 Blog Track

_Kang Liu, Gen Wang, Xianpei Han, Jun Zhao_

- :fontawesome-solid-user-group: **Participant:** [cas-liu-nlpr-iacas](./participants.md#cas-liu-nlpr-iacas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/cas.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/cas.blog.final.pdf)
- :material-file-search: **Runs:** [NLPRPT](./runs.md#nlprpt) | [NLPRPTD1](./runs.md#nlprptd1) | [NLPRPTD2](./runs.md#nlprptd2) | [NLPRPST](./runs.md#nlprpst) | [NLPRTD](./runs.md#nlprtd) | [NLPRPTONLY](./runs.md#nlprptonly)

??? abstract "Abstract"
	
	This paper describes the opinion retrieval system for TREC 2007 blog track. This paper focuses on two components of the system. One component is important content block detection component which is used to extract blog contents and get rid of noises in blog pages. Another component is opinion retrieval component which is used to give each sentence an opinion score and combine it with topic score based on SVR. The evaluation proves the validity of our algorithm in the task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuWHZ07.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuWHZ07,
		author = {Kang Liu and Gen Wang and Xianpei Han and Jun Zhao},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{NLPR} in {TREC} 2007 Blog Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/cas.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiuWHZ07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The Robert Gordon University at the Opinion Retrieval Task of the  2007 TREC Blog Track

_Rahman Mukras, Nirmalie Wiratunga, Robert Lothian_

- :fontawesome-solid-user-group: **Participant:** [robert-gordonu.mukras](./participants.md#robert-gordonu.mukras)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/robert-gordonu.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/robert-gordonu.blog.final.pdf)
- :material-file-search: **Runs:** [rgu0](./runs.md#rgu0) | [rgu1](./runs.md#rgu1) | [rgu2](./runs.md#rgu2) | [rgu3](./runs.md#rgu3) | [rgu4](./runs.md#rgu4)

??? abstract "Abstract"
	
	The Robert Gordon University (RGU) participated in the Opinion Retrieval Task of the Trec 2007 Blog Track. At the core of the system we developed is a set of training documents labeled with respect to opinion. These documents are used to train a classifier in order to classify the documents that are relevant to the given Trec topics. However, a major limitation with these training documents is that they are not always generic enough to serve as good training examples for all the 50 Trec topics. We therefore propose a solution that generalizes their content by exploiting the context of opinion related language constructs such as adjectives, verbs, and adverbs. Our system significantly improves over RGU's previous Blog Track systems.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MukrasWL07.bib) "
	```
	@inproceedings{DBLP:conf/trec/MukrasWL07,
		author = {Rahman Mukras and Nirmalie Wiratunga and Robert Lothian},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The Robert Gordon University at the Opinion Retrieval Task of the 2007 {TREC} Blog Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/robert-gordonu.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MukrasWL07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploring Traits of Adjectives to Predict Polarity Opinion in Blogs  and Semantic Filters in Genomics

_Miguel E. Ruiz, Ying Sun, Jianqiang Wang, Hongfang Liu_

- :fontawesome-solid-user-group: **Participant:** [ubuffalo.ruiz](./participants.md#ubuffalo.ruiz)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/unorth-texas.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/unorth-texas.blog.final.pdf)
- :material-file-search: **Runs:** [UB1](./runs.md#ub1) | [pUB11](./runs.md#pub11) | [pUB12](./runs.md#pub12) | [UB2](./runs.md#ub2) | [pUB21](./runs.md#pub21) | [UB3](./runs.md#ub3) | [pUB32](./runs.md#pub32)

??? abstract "Abstract"
	
	This paper presents the results of our team in the Genomics and Blog tracks in TREC 2007. We used the language model implementation provided by Indri for both tracks. For the BLOG track we explored the use of adjectives with in a post as a way to predict opinion polarity. Our work in the Genomics track explores two approaches to generate queries from the original topics. The first approach performs automatic term expansion using UMLS to generate a structured query that can be submitted using Indri's query language. The second approach uses a query expansion and re-ranking method based on identification of semantic relatives. This approach tries to capture the semantic of the potential answer, key terms in the topic and detection of gene/protein terms mentioned in the topic.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RuizSWL07.bib) "
	```
	@inproceedings{DBLP:conf/trec/RuizSWL07,
		author = {Miguel E. Ruiz and Ying Sun and Jianqiang Wang and Hongfang Liu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Exploring Traits of Adjectives to Predict Polarity Opinion in Blogs and Semantic Filters in Genomics},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/unorth-texas.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RuizSWL07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2007 Blog Track Experiments at Kobe University

_Kazuhiro Seki, Yoshihiro Kino, Shohei Sato, Kuniaki Uehara_

- :fontawesome-solid-user-group: **Participant:** [kobeu.seki](./participants.md#kobeu.seki)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/kobeu.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/kobeu.blog.final.pdf)
- :material-file-search: **Runs:** [Ku](./runs.md#ku) | [KuKnn](./runs.md#kuknn) | [KuS](./runs.md#kus) | [KuSvm](./runs.md#kusvm) | [KuSvmS](./runs.md#kusvms) | [kud](./runs.md#kud) | [kudn](./runs.md#kudn) | [kudsn](./runs.md#kudsn) | [kuds](./runs.md#kuds)

??? abstract "Abstract"
	
	This paper describes our approaches to the opinion retrieval and blog distillation tasks for the Blog Track. For opinion retrieval we employ a two-stage framework consisting of keyword search and opinion classification, where customer reviews collected from Amazon.com are used for feature selection. For the blog distillation task we consider all the blog posts belonging to a blog in order to estimate the relevance of the blog at large. To accomplish this, we first identify relevant blogs for a given topic by keyword search and then examine all the posts for each identified blog. In addition, we attempt to detect and discard spam blogs (splogs) and non-English blogs to improve system performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SekiKSU07.bib) "
	```
	@inproceedings{DBLP:conf/trec/SekiKSU07,
		author = {Kazuhiro Seki and Yoshihiro Kino and Shohei Sato and Kuniaki Uehara},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2007 Blog Track Experiments at Kobe University},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/kobeu.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SekiKSU07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass at TREC 2007 Blog Distillation Task

_Jangwon Seo, W. Bruce Croft_

- :fontawesome-solid-user-group: **Participant:** [umass.allan](./participants.md#umass.allan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/umass.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/umass.blog.final.pdf)
- :material-file-search: **Runs:** [UMaTiGR](./runs.md#umatigr) | [UMaTiPCS](./runs.md#umatipcs) | [UMaTiPCSwGR](./runs.md#umatipcswgr) | [UMaTDPCSwGR](./runs.md#umatdpcswgr)

??? abstract "Abstract"
	
	The focus of the blog distillation task is finding blogs with a principle, recurring interest in a specific topic. For this task, we considered a blog as a collection of postings and used resource selection approaches. Further, we investigated techniques that penalized general blogs and combined resource selection techniques. This combination demonstrated significant improvements over baselines.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SeoC07.bib) "
	```
	@inproceedings{DBLP:conf/trec/SeoC07,
		author = {Jangwon Seo and W. Bruce Croft},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {UMass at {TREC} 2007 Blog Distillation Task},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/umass.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SeoC07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DUTIR at TREC 2007 Blog Track

_Rui Song, Qin Tang, Daming Shi, Hongfei Lin, Zhihao Yang_

- :fontawesome-solid-user-group: **Participant:** [dalianu.yang](./participants.md#dalianu.yang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/dalianu.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/dalianu.blog.final.pdf)
- :material-file-search: **Runs:** [DUTRun1](./runs.md#dutrun1) | [DUTRun4](./runs.md#dutrun4) | [DUTRun4P](./runs.md#dutrun4p) | [DUTRun5](./runs.md#dutrun5) | [DUTRun5P](./runs.md#dutrun5p) | [DUTRun2](./runs.md#dutrun2) | [DUTRun1P](./runs.md#dutrun1p) | [DUTRun2P](./runs.md#dutrun2p) | [DUTRun3](./runs.md#dutrun3) | [DUTRun3P](./runs.md#dutrun3p) | [DUTRun6](./runs.md#dutrun6) | [DUTRun6P](./runs.md#dutrun6p) | [DUTDRun1](./runs.md#dutdrun1) | [DUTDRun2](./runs.md#dutdrun2) | [DUTDRun3](./runs.md#dutdrun3) | [DUTDRun4](./runs.md#dutdrun4)

??? abstract "Abstract"
	
	This paper describes DUTIR at TREC 2007 Blog Track. In data preprocessing, a non English language list created from the corpus was used to remove the non English blogs, blog templates were also used to extract the post and comment; in Opinion Retrieval task, information in the meta tags were also indexed; in the polarity subtask, a method based on SVM was used and the Information Gain attribute selecting method was used to assist SVM; in Feed Distillation task, three type of feeds were analyzed according to their tag structure, information extracted from particular tags of the feeds were finally indexed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SongQSLY07.bib) "
	```
	@inproceedings{DBLP:conf/trec/SongQSLY07,
		author = {Rui Song and Qin Tang and Daming Shi and Hongfei Lin and Zhihao Yang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DUTIR} at {TREC} 2007 Blog Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/dalianu.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SongQSLY07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Subjective Adjectives in Opinion Retrieval from Blogs

_Olga Vechtomova_

- :fontawesome-solid-user-group: **Participant:** [uwaterloo-olga](./participants.md#uwaterloo-olga)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uwaterloo.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uwaterloo.blog.final.pdf)
- :material-file-search: **Runs:** [UWbaseTerms](./runs.md#uwbaseterms) | [UWbasePhrase](./runs.md#uwbasephrase) | [UWopinion1](./runs.md#uwopinion1) | [UWopinion2](./runs.md#uwopinion2) | [UWopinion3](./runs.md#uwopinion3) | [UWopinion4](./runs.md#uwopinion4)

??? abstract "Abstract"
	
	The University of Waterloo participated in the opinion finding task of the Blog track. The task consists of finding blog posts (documents) containing an opinion expressed about the subject of the query. Each query represents a single “entity” that can be, for example, a person, product name, abstract concept, location or event. The relevance judgements were done on a 5-point scale: -1 - not judged, 0 - non-relevant, 1 - relevant, 2 - relevant, negative opinion; 3 - relevant, mixed positive and negative opinion, 4 - relevant, positive opinion. While many elements in the language can be used to express subjective contents, adjectives are one of the major means of expressing value judgement in English. Our approach consists in using a list of 1336 subjective adjectives manually constructed by Hatzivassiloglou and McKeown [2] for identifying opinionated contents. We hypothesise that presence of subjective adjectives within fixed-size windows around query term instances in a document is a useful feature for finding opinions directed at the query concept.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Vechtomova07.bib) "
	```
	@inproceedings{DBLP:conf/trec/Vechtomova07,
		author = {Olga Vechtomova},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Using Subjective Adjectives in Opinion Retrieval from Blogs},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uwaterloo.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Vechtomova07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WIDIT in TREC 2007 Blog Track: Combining Lexicon-Based Methods  to Detect Opinionated Blogs

_Kiduk Yang, Ning Yu, Hui Zhang_

- :fontawesome-solid-user-group: **Participant:** [indianau.yang](./participants.md#indianau.yang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/indianau.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/indianau.blog.final.pdf)
- :material-file-search: **Runs:** [oqlr2f2opt](./runs.md#oqlr2f2opt) | [oqlr2fopt](./runs.md#oqlr2fopt) | [oqlr2f2](./runs.md#oqlr2f2) | [oqlnr2opt](./runs.md#oqlnr2opt) | [oqsnr2opt](./runs.md#oqsnr2opt) | [oqsnr1Base](./runs.md#oqsnr1base) | [oqlr2f2optP](./runs.md#oqlr2f2optp) | [oqlr2foptP](./runs.md#oqlr2foptp) | [oqlr2f2P](./runs.md#oqlr2f2p) | [oqlnr2optP](./runs.md#oqlnr2optp) | [oqsnr2optP](./runs.md#oqsnr2optp)

??? abstract "Abstract"
	
	In TREC-2007, Indiana University‟s WIDIT Lab1 participated in the Blog track‟s opinion task and the polarity subtask. For the opinion task, whose goal is to 'uncover the public sentiment towards a given entity/target', we focused on combining multiple sources of evidence to detect opinionated blog postings. Since detecting opinionated blogs on a given topic (i.e., entity/target) involves not only retrieving topically relevant blogs but also identifying those that contain opinions about the target, our approach to the opinion finding task consisted of first applying traditional IR methods to retrieve on-topic blogs and then boosting the ranks of opinionated blogs based on combined opinion scores generated by multiple opinion detection methods. The key idea underlying our opinion detection method is to rely on a variety of complementary evidences rather than trying to optimize a single approach. This fusion approach to opinionated blog detection is motivated by our past experience that suggested no single approach, whether lexicon-based or classifier-driven, is well-suited for the blog opinion retrieval task. To accomplish the polarity subtask, which requires classification of the retrieved blogs into positive or negative orientation, our opinion detection module was extended to generate polarity scores to be used for polarity determination.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangYZ07.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangYZ07,
		author = {Kiduk Yang and Ning Yu and Hui Zhang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WIDIT} in {TREC} 2007 Blog Track: Combining Lexicon-Based Methods to Detect Opinionated Blogs},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/indianau.blog.final.pdf},
		timestamp = {Wed, 29 Jun 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/YangYZ07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### FDU at TREC 2007: Opinion Retrieval of Blog Track

_Qi Zhang, Bingqing Wang, Lide Wu, Xuanjing Huang_

- :fontawesome-solid-user-group: **Participant:** [fudanu.wu](./participants.md#fudanu.wu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/fudan.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/fudan.blog.final.pdf)
- :material-file-search: **Runs:** [FDUNoOpTisd](./runs.md#fdunooptisd) | [FDUNOpRSVMT](./runs.md#fdunoprsvmt) | [FDUTisdOpSVM](./runs.md#fdutisdopsvm) | [FDUNoOpTSem](./runs.md#fdunooptsem) | [FDUTOSVMSem](./runs.md#fdutosvmsem) | [FDUTNRSVMSem](./runs.md#fdutnrsvmsem)

??? abstract "Abstract"
	
	This paper describes our participation in the opinion retrieval task at Blog Track 07. The system consisted of the preprocess part, the topic retrieval part and sentiment analysis part. In the topic retrieval part, we adopted pseudo-relevance feedback and a novel approach to form a modified query. In the sentiment analysis part, each blog post was given an opinion score based on the sentences contained in this post. The subjectivity of each sentence was predicted by a CME classifier. Then the blog posts were reranked based on the similarity given by the topic retrieval and the opinion score given by the sentiment analysis.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangWWH07.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangWWH07,
		author = {Qi Zhang and Bingqing Wang and Lide Wu and Xuanjing Huang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{FDU} at {TREC} 2007: Opinion Retrieval of Blog Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/fudan.blog.final.pdf},
		timestamp = {Thu, 23 Mar 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangWWH07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UIC at TREC 2007 Blog Track

_Wei Zhang, Clement T. Yu_

- :fontawesome-solid-user-group: **Participant:** [uiuc-zhang](./participants.md#uiuc-zhang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/uic-zhang.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/uic-zhang.blog.final.pdf)
- :material-file-search: **Runs:** [uic1c](./runs.md#uic1c) | [uic1s](./runs.md#uic1s) | [uic75c](./runs.md#uic75c) | [uic75s](./runs.md#uic75s) | [uic1cpnm](./runs.md#uic1cpnm) | [uic1spnm](./runs.md#uic1spnm) | [uic75cpnm](./runs.md#uic75cpnm) | [uic75spnm](./runs.md#uic75spnm)

??? abstract "Abstract"
	
	In TREC 2007 Blog Track, we developed a three-step algorithm for the opinion retrieval task. An information retrieval step retrieves the query-relevant documents. A following opinion identification step identifies the opinionative texts in these documents. A ranking step identifies the query-related opinions in the documents and ranks them by calculating their opinion similarity scores. For the polarity task, our strategy is to find the positive and negative documents respectively, and then find the mixed opinionative documents in the intersection of the positive and negative document sets. We implemented our opinion retrieval algorithm in two special cases, one to retrieve the positive documents, and the other to retrieve the negative documents. A judging function labeled a subset of the documents, which were in the intersection of the positive and negative documents, as the mixed opinionative documents. We studied two parameters in our opinion retrieval algorithm, each of which had two values to compare. This resulted in four submitted opinion retrieval runs and their corresponding polarity runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangY07.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangY07,
		author = {Wei Zhang and Clement T. Yu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UIC} at {TREC} 2007 Blog Track},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/uic-zhang.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangY07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WHU at Blog Track 2007

_Haozhen Zhao, Zhicheng Luo, Wei Lu_

- :fontawesome-solid-user-group: **Participant:** [wuhanu.lu](./participants.md#wuhanu.lu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/wuhanu.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/wuhanu.blog.final.pdf)
- :material-file-search: **Runs:** [NOOPWHU1](./runs.md#noopwhu1) | [OTWHU101](./runs.md#otwhu101) | [OTWHU102](./runs.md#otwhu102) | [OTPSWHU101](./runs.md#otpswhu101) | [OTPSWHU102](./runs.md#otpswhu102) | [TDWHU100](./runs.md#tdwhu100) | [TDWHU101](./runs.md#tdwhu101) | [TDWHU201](./runs.md#tdwhu201) | [TDWHU200](./runs.md#tdwhu200)

??? abstract "Abstract"
	
	We participate in all the sub tracks of the Blog track 2007. For the Opinionated Task, we use an excerpt list of the SentiWordNet to determine the opinionated nature of returned blog posts. For the Topic distillation Task, we test the effectiveness of cleaning work for the data collection in improvement of retrieval performance and the use of title and description part as queries. Both results show that our method does not work well.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhaoLL07.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhaoLL07,
		author = {Haozhen Zhao and Zhicheng Luo and Wei Lu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WHU} at Blog Track 2007},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/wuhanu.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhaoLL07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Topic Categorization for Relevancy and Opinion Detection

_GuangXu Zhou, Hemant Joshi, Coskun Bayrak_

- :fontawesome-solid-user-group: **Participant:** [uarkansas-littlerock.bayrak](./participants.md#uarkansas-littlerock.bayrak)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec16/papers/ualr.blog.final.pdf](http://trec.nist.gov/pubs/trec16/papers/ualr.blog.final.pdf)
- :material-file-search: **Runs:** [UALR07Base](./runs.md#ualr07base) | [UALR07BlogIU](./runs.md#ualr07blogiu) | [UALR07TDN](./runs.md#ualr07tdn) | [UALR07IU2](./runs.md#ualr07iu2) | [UALR07CML](./runs.md#ualr07cml) | [UALR07Text](./runs.md#ualr07text)

??? abstract "Abstract"
	
	University of Arkansas at Little Rock's Blog Track team participated in only the core task of the blog track this year. The data acquired was identical to that of previous year except some new .retrieval tasks were introduced. The core task was to identify blogs that are opinionated about a certain subject. Fifty new topics were provided by National Institute of Standards and Technology (NIST) this year. Apart from the core task, two subtasks were also introduced. Polarity subtask was to detect polarity of the opinionated blog about a given topic. Feed distillation subtask was based on finding feeds rather than individual permalinks. Last year, we participated in the core task [1] and this year we planned to continue on our previous work. Although an attempt was made last year to use Active Learning with Support Vector Machine (SVM) to detect opinionated blog, identifying the opinion expressed about a given topic was unsuccessful. The difference this time around is in the use of search engines to conduct the topic search, categorizations of queries for further training, and a Natural Language based “one-pass-processing” approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhouJB07.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhouJB07,
		author = {GuangXu Zhou and Hemant Joshi and Coskun Bayrak},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Topic Categorization for Relevancy and Opinion Detection},
		booktitle = {Proceedings of The Sixteenth Text REtrieval Conference, {TREC} 2007, Gaithersburg, Maryland, USA, November 5-9, 2007},
		series = {{NIST} Special Publication},
		volume = {500-274},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2007},
		url = {http://trec.nist.gov/pubs/trec16/papers/ualr.blog.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhouJB07.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

