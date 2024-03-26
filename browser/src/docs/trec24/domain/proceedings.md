# Proceedings - Dynamic Domain 2015 

#### TREC 2015 Dynamic Domain Track Overview

_Hui Yang, John R. Frank, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [https://trec.nist.gov/pubs/trec24/papers/overview-dd.pdf](https://trec.nist.gov/pubs/trec24/papers/overview-dd.pdf)
??? abstract "Abstract"
	
	Search tasks for professional searchers, such as law enforcement agencies, police officers, and patent examiners, are often more complex than open domain Web search tasks. When professional searchers look for relevant information, it is often the case that they need to go through multiple iterations of searches to interact with a system. The Dynamic Domain Track supports research in dynamic, exploratory search within complex information domains. By providing real-time fine-grained feedback with relevance judgments that was collected during assessing time to the participating systems, we create a dynamic and iterative search process that lasts until the system decides to stop. The search systems are expected to be able to adjust their retrieval algorithms based on the feedback and find quickly relevant information for a multi-faceted information need. This document reports the task, datasets, topic and assessment creation, submissions, and evaluation results for the TREC 2015 Dynamic Domain (DD) Track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/0001FS15.bib) "
	```
	@inproceedings{DBLP:conf/trec/0001FS15,
		author = {Hui Yang and John R. Frank and Ian Soboroff},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} 2015 Dynamic Domain Track Overview},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {https://trec.nist.gov/pubs/trec24/papers/overview-dd.pdf},
		timestamp = {Wed, 03 Feb 2021 08:31:23 +0100},
		biburl = {https://dblp.org/rec/conf/trec/0001FS15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC Dynamic Domain: Polar Science

_Annie Bryant Burgess, Chris Mattmann, Giuseppe Totaro, Lewis John McGibbney, Paul M. Ramirez_

- :fontawesome-solid-user-group: **Participant:** [JPL_USC](./participants.md#jpl_usc)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/JPL_USC-DD.pdf](http://trec.nist.gov/pubs/trec24/papers/JPL_USC-DD.pdf)

??? abstract "Abstract"
	
	This paper outlines the creation of the Polar dataset within the TREC-Dynamic Domain track. The techniques used to create the Polar dataset fall into two basic categories: information extraction using Apache Tika and information retrieval using Apache Nutch. Frist, we expanded the parsing capabilities of Apache Tika, an open source framework for text and metadata extraction, to provide more searchable content within Polar data repositories. Second, we used Apache Nutch, a distributed search engine that runs on top of Apache Hadoop, to crawl three prominent Polar data repositories: the National Science Foundation Advanced Cooperative Arctic Data and Information System (ACADIS), the National Snow and Ice Data Center (NSIDC) Arctic Data Explorer (ADE), and the National Aeronautics and Space Administration Antarctic Master Directory (AMD). Because finding data is often a primary challenge in scientific discovery, the inclusion of the Polar dataset in TREC-DD helps advance science through data discovery and provides TREC-DD a new challenge in in the realm of search relevancy.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BurgessMTMR15.bib) "
	```
	@inproceedings{DBLP:conf/trec/BurgessMTMR15,
		author = {Annie Bryant Burgess and Chris Mattmann and Giuseppe Totaro and Lewis John McGibbney and Paul M. Ramirez},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {{TREC} Dynamic Domain: Polar Science},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/JPL\_USC-DD.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BurgessMTMR15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Laval University and Lakehead University at TREC Dynamic Domain  2015: Combination of Techniques for Subtopics Coverage

_Robin Joganah, Luc Lamontagne, Richard Khoury_

- :fontawesome-solid-user-group: **Participant:** [LavallVA](./participants.md#lavallva)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/LavallVA-DD.pdf](http://trec.nist.gov/pubs/trec24/papers/LavallVA-DD.pdf)

??? abstract "Abstract"
	
	This paper describes the joint submission by Laval University and Lakehead University to the TREC 2015 Dynamic Domain track. We submitted four runs for the main track and one run for the judged-only track. In our view, the Dynamic Domain process can be separated into two phases: a traditional static information retrieval phase to generate an initial set of documents, followed by a dynamic information retrieval phase which takes user feedback into account to improve the results. We developed an algorithm that combines keyword search, Latent Dirichlet Allocation, and K-Means clustering to take advantage of each technique to generate the best subset of results for the user. Our systems performed mostly over the median of the group of participants and our system for the “judged-only” task had the best score for a wide range of queries.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JoganahLK15.bib) "
	```
	@inproceedings{DBLP:conf/trec/JoganahLK15,
		author = {Robin Joganah and Luc Lamontagne and Richard Khoury},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Laval University and Lakehead University at {TREC} Dynamic Domain 2015: Combination of Techniques for Subtopics Coverage},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/LavallVA-DD.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JoganahLK15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Re-ranking via User Feedback: Georgetown University at TREC 2015  DD Track

_Jiyun Luo, Hui Yang_

- :fontawesome-solid-user-group: **Participant:** [georgetown](./participants.md#georgetown)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/georgetown_ir-DD.pdf](http://trec.nist.gov/pubs/trec24/papers/georgetown_ir-DD.pdf)
- :material-file-search: **Runs:** [GU_RUN3_SIMI](./runs.md#gu_run3_simi) | [GU_RUN4_SIMI](./runs.md#gu_run4_simi)

??? abstract "Abstract"
	
	There are two principal components involved in a search process, the user and the search engine. In TREC DD, the user is modeled by a simulator, called “jig”. The jig and the search engine exchange many messages among themselves, including the relevant passages returned by the jig, user cost spent on examining the documents, etc. In this work, we don't apply any dynamic search algorithms to model these interactions. Instead, we produce a basic re-ranking baseline. Our algorithm starts at taking in an initial query from the simulator. During the search, we collect the relevance feedback from the simulator and use them to re-rank the initial retrieval results. Our algorithm terminates itself automatically when it senses that the user has gained enough information about the search topic or that no further relevant documents can be retrieved for the user.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LuoY15.bib) "
	```
	@inproceedings{DBLP:conf/trec/LuoY15,
		author = {Jiyun Luo and Hui Yang},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {Re-ranking via User Feedback: Georgetown University at {TREC} 2015 {DD} Track},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/georgetown\_ir-DD.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LuoY15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### University of Glasgow at TREC 2015: Experiments with Terrier in  Contextual Suggestion, Temporal Summarisation and Dynamic Domain Tracks

_Richard McCreadie, Saul Vargas, Craig MacDonald, Iadh Ounis, Stuart Mackie, Jarana Manotumruksa, Graham McDonald_

- :fontawesome-solid-user-group: **Participant:** [uogTr](./participants.md#uogtr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec24/papers/uogTr-CXTSDD.pdf](http://trec.nist.gov/pubs/trec24/papers/uogTr-CXTSDD.pdf)
- :material-file-search: **Runs:** [uogTrEpsilonG](./runs.md#uogtrepsilong) | [uogTrRR](./runs.md#uogtrrr) | [uogTrSI](./runs.md#uogtrsi) | [uogTrIL](./runs.md#uogtril) | [uogTrxQuADRR](./runs.md#uogtrxquadrr)

??? abstract "Abstract"
	
	In TREC 2015, we focus on tackling the challenges posed by the Contextual Suggestion, Temporal Summarisation and Dynamic Domain tracks. For Contextual Suggestion, we investigate the use of user-generated data in location-based social networks (LBSN) to suggest venues. For Temporal Summarisation, we examine features for event summarisation that explicitly model the entities involved in the events. Meanwhile, for the Dynamic Domain track, we explore resource selection techniques for identifying the domain of interest and diversifying sub-topic intents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/McCreadieVMOMMM15.bib) "
	```
	@inproceedings{DBLP:conf/trec/McCreadieVMOMMM15,
		author = {Richard McCreadie and Saul Vargas and Craig MacDonald and Iadh Ounis and Stuart Mackie and Jarana Manotumruksa and Graham McDonald},
		editor = {Ellen M. Voorhees and Angela Ellis},
		title = {University of Glasgow at {TREC} 2015: Experiments with Terrier in Contextual Suggestion, Temporal Summarisation and Dynamic Domain Tracks},
		booktitle = {Proceedings of The Twenty-Fourth Text REtrieval Conference, {TREC} 2015, Gaithersburg, Maryland, USA, November 17-20, 2015},
		series = {{NIST} Special Publication},
		volume = {500-319},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2015},
		url = {http://trec.nist.gov/pubs/trec24/papers/uogTr-CXTSDD.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/McCreadieVMOMMM15.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

