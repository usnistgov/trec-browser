# Proceedings - Knowledge Base Acceleration 2012 

#### Building an Entity-Centric Stream Filtering Test Collection for TREC  2012

_John R. Frank, Max Kleiman-Weiner, Daniel A. Roberts, Feng Niu, Ce Zhang, Christopher Ré, Ian Soboroff_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/KBA.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec21/papers/KBA.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The Knowledge Base Acceleration track in TREC 2012 focused on a single task: filter a time-ordered corpus for documents that are highly relevant to a predefined list of entities. KBA differs from previous filtering evaluations in two primary ways: the stream corpus is >100x larger than previous filtering collections, and the use of entities as topics enables systems to incorporate structured knowledge bases (KB), such as Wikipedia, as external data sources. A successful KBA system must do more than resolve the meaning of entity mentions by linking documents to the KB: it must also distinguish centrally relevant documents that are worth citing in the entity's WP article. This combines thinking from natural language processing (NLP) and information retrieval (IR). Filtering tracks in TREC have typically used queries based on topics described by a set of keyword queries or short descriptions, and annotators have generated relevance judgments based on their personal interpretation of the topic. For TREC 2012, we selected a set of filter topics based on Wikipedia entities: 27 people and 2 organizations. Such named entities are more familiar in NLP than IR. We also constructed an entirely new stream corpus spanning 4,973 consecutive hours from October 2011 through April 2012. It contains over 400M documents, which we augmented with named entity classification tagging for the ~40% of the documents identified as English. Each document has a timestamp that places it in the stream. The 29 target entities were mentioned infrequently enough in the corpus that NIST assessors could judge the relevance of most of the mentioning documents (~91%). Judgments for documents from before January 2012 were provided to TREC teams as training data for filtering documents from the remaining hours. Run submissions were evaluated against the assessor-generated list of citation-worthy documents. We present peak F_1 scores averaged across the entities for all run submissions. High scoring systems used a variety of approaches, including simple name matching, names of related entities from the knowledge base, and support vector machines. Top scoring systems achieved F_1 scores in the high 30s or low 40s depending on score averaging techniques. We discuss key lessons learned at the end of the paper.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/FrankKRNZRS12.bib) "
	```
	@inproceedings{DBLP:conf/trec/FrankKRNZRS12,
		author = {John R. Frank and Max Kleiman{-}Weiner and Daniel A. Roberts and Feng Niu and Ce Zhang and Christopher R{\'{e}} and Ian Soboroff},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Building an Entity-Centric Stream Filtering Test Collection for {TREC} 2012},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/KBA.OVERVIEW.pdf},
		timestamp = {Tue, 12 Jan 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/FrankKRNZRS12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Amsterdam at TREC 2012

_Richard Berendsen, Edgar Meij, Daan Odijk, Maarten de Rijke, Wouter Weerkamp_

- :fontawesome-solid-user-group: **Participant:** [UvA](./participants.md#uva)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/UvA.microblog.kba.final.pdf](http://trec.nist.gov/pubs/trec21/papers/UvA.microblog.kba.final.pdf)
- :material-file-search: **Runs:** [UvA-UvAbaseline](./runs.md#uva-uvabaseline) | [UvA-UvALearning](./runs.md#uva-uvalearning) | [UvA-UvAIncLearnHigh](./runs.md#uva-uvainclearnhigh) | [UvA-UvAIncLearnLow](./runs.md#uva-uvainclearnlow) | [UvA-UvAIncLearnT25](./runs.md#uva-uvainclearnt25) | [UvA-UvAIncLearnT50](./runs.md#uva-uvainclearnt50)

??? abstract "Abstract"
	
	We describe the participation of the University of Amsterdam's ILPS group in the Knowledge Base Acceleration and Microblog tracks at TREC 2012.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BerendsenMORW12.bib) "
	```
	@inproceedings{DBLP:conf/trec/BerendsenMORW12,
		author = {Richard Berendsen and Edgar Meij and Daan Odijk and Maarten de Rijke and Wouter Weerkamp},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Amsterdam at {TREC} 2012},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/UvA.microblog.kba.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BerendsenMORW12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### LSIS/LIA at TREC 2012 Knowledge Base Acceleration

_Ludovic Bonnefoy, Vincent Bouvier, Patrice Bellot_

- :fontawesome-solid-user-group: **Participant:** [LSIS](./participants.md#lsis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/LSIS.LIA.kba.final.pdf](http://trec.nist.gov/pubs/trec21/papers/LSIS.LIA.kba.final.pdf)
- :material-file-search: **Runs:** [LSIS-lsisSys1](./runs.md#lsis-lsissys1) | [LSIS-lsisSys2](./runs.md#lsis-lsissys2) | [LSIS-lsisRFAll](./runs.md#lsis-lsisrfall) | [LSIS-lsisRFYes](./runs.md#lsis-lsisrfyes) | [LSIS-lsisSRFYes](./runs.md#lsis-lsissrfyes) | [LSIS-lsisSRFAll](./runs.md#lsis-lsissrfall)

??? abstract "Abstract"
	
	This paper describes our joint participation in the TREC 2012 KBA task. The system is broken down as follows : first name variations of the entity topics are searched then documents containing at least one of them are retrieved. Finally documents go through two classifiers to categorize them as garbage, neutrals, relevant or centrals. This system got good results (3rd of 11) however first analyses tends to show that ranking is just a little bit better than random.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BonnefoyBB12.bib) "
	```
	@inproceedings{DBLP:conf/trec/BonnefoyBB12,
		author = {Ludovic Bonnefoy and Vincent Bouvier and Patrice Bellot},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{LSIS/LIA} at {TREC} 2012 Knowledge Base Acceleration},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/LSIS.LIA.kba.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BonnefoyBB12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Bi-directional Linkability From Wikipedia to Documents and Back Again:  UMass at TREC 2012 Knowledge Base Acceleration Track

_Jeffrey Dalton, Laura Dietz_

- :fontawesome-solid-user-group: **Participant:** [UMass_CIRR](./participants.md#umass_cirr)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/umass_CIRR.kba.final.pdf](http://trec.nist.gov/pubs/trec21/papers/umass_CIRR.kba.final.pdf)

??? abstract "Abstract"
	
	This notebook details the participation of the University of Massachusetts Amherst in the Cumulative Citation Recommendation task (CCR) of the TREC 2012 Knowledge Base Acceleration Track. UMass' objective is to introduce a single model for Knowledge Base Entity Linking and Knowledge Base Acceleration stream filtering using bi-directional linkability between knowledge base (KB) entries and mentions of the entities in documents. Our system focuses on estimating linkability between documents and Knowledge Base entities which measures compatibility in two directions: (1) from a KB entity to documents and (2) from mentions of entities in documents to their KB entries. The entity to document direction, is modeled as a retrieval task where the goal is to identify the most relevant documents for an entity in the evaluation time range. However, if the entity is ambiguous, the retrieved documents may contain documents that are relevant to other entities with the same or similar name. To address this, we want to leverage information from the document to disambiguate the entity. We observe that this problem, from mention to KB entity, is very similar to the TAC Knowledge Base Population Entity Linking Task (Ji et al., 2011). The major goal of our participation is to explore how these two directions, from KB to documents and back can be combined. For KBA, the goal is to identify documents from a stream that are central for a given entity in Wikipedia. Some participants viewed this as a classification problem and trained supervised classifiers for each entity. Instead, our approach to the problem is based upon document ranking. We combine probabilistic information retrieval and then combine the results with TAC entity linking for re-ranking and filtering. Our ranking approach has three stages: First, documents are retrieved from the stream corpus using an entity query model. Second, potential mentions of the target entity are identified in the retrieved documents. Third, links between the document mentions and the target entity are established or dismissed, giving rise to a filtered (or reranked) list of results that mention the target entity. Our initial system leverages the bi-directional relevance as a simple form of re-ranking of retrieved documents, but we envision tighter integration in the future. The baseline retrieval run generates a query from the Wikipedia KB entry, including the name, name variants, and linked entities. We also incorporate contextual evidence from the document stream by using the documents in the training time period as relevance feedback documents. We use Latent Concept Expansion (Metzler and Croft, 2007) to estimate important contextual words and NER concepts. Our experiments show that incorporating entity context from query expansion methods provides significant gains both in precision and recall over the baseline, with all of our experimental runs outperforming the median. Our best performing run incorporates linkability evidence from the TAC Entity Linking model.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DaltonD12.bib) "
	```
	@inproceedings{DBLP:conf/trec/DaltonD12,
		author = {Jeffrey Dalton and Laura Dietz},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Bi-directional Linkability From Wikipedia to Documents and Back Again: UMass at {TREC} 2012 Knowledge Base Acceleration Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/umass\_CIRR.kba.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DaltonD12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The University of Illinois' Graduate School of Library and Information  Science at TREC 2012

_Miles Efron, Jana Deisner, Peter Organisciak, Garrick Sherman, Ana Lucic_

- :fontawesome-solid-user-group: **Participant:** [uiucGSLIS](./participants.md#uiucgslis)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/uiucGSLIS.microblog.kba.final.pdf](http://trec.nist.gov/pubs/trec21/papers/uiucGSLIS.microblog.kba.final.pdf)
- :material-file-search: **Runs:** [uiucGSLIS-gslis_adaptive](./runs.md#uiucgslis-gslis_adaptive) | [uiucGSLIS-gslis_mult](./runs.md#uiucgslis-gslis_mult)

??? abstract "Abstract"
	
	The University of Illinois' Graduate School of Library and Information Science (uiucGSLIS) participated in TREC's microblog and knowledge base acceleration (KBA) tracks in 2012. Our high-level goals were two-fold: Microblog: Test a novel method for document ranking during real-time search. KBA: Compare methods of topic representation-particularly longitudinal adaptation of topic representation-for the KBA task. Our document ranking in the microblog track is based on a behavioral metaphor. Given a query Q, we decompose Q into a set of imaginary saved searches S. Given an incoming document stream D = D1, D2, . . . , DN , we ask: what is the probability that a document D is read, given the user's query and a rational allocation of attention over his saved searches? [...]
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EfronDOSL12.bib) "
	```
	@inproceedings{DBLP:conf/trec/EfronDOSL12,
		author = {Miles Efron and Jana Deisner and Peter Organisciak and Garrick Sherman and Ana Lucic},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The University of Illinois' Graduate School of Library and Information Science at {TREC} 2012},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/uiucGSLIS.microblog.kba.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EfronDOSL12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Team Association Analysis for Named Entity Filtering

_Oskar Gross, Hannu Toivonen, Antoine Doucet_

- :fontawesome-solid-user-group: **Participant:** [helsinki](./participants.md#helsinki)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/helsinki.kba.final.pdf](http://trec.nist.gov/pubs/trec21/papers/helsinki.kba.final.pdf)
- :material-file-search: **Runs:** [helsinki-disgraph](./runs.md#helsinki-disgraph) | [helsinki-disgraph2](./runs.md#helsinki-disgraph2)

??? abstract "Abstract"
	
	This paper describes the participation of the Universities of Helsinki and Caen in the first round of the TREC Knowledge Base Acceleration track3. The task focused on filtering a stream of documents relevant to a set of entities. Our approach uses word co-occurrence graphs for modelling the named entities. We submitted two runs that achieved an average F-measure superior to the mean of all submitted runs. The best of those runs ranked in the top 5 runs for both the central and relevant F-measures, out of a total of 43 runs submitted by 11 institutions. As our runs were the produce of a first implementation of our approach, these preliminary results are very supportive of our idea to use concept graphs for modelling named entity relations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GrossTD12.bib) "
	```
	@inproceedings{DBLP:conf/trec/GrossTD12,
		author = {Oskar Gross and Hannu Toivonen and Antoine Doucet},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Team Association Analysis for Named Entity Filtering},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/helsinki.kba.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GrossTD12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The HLTCOE Approach to the TREC 2012 KBA Track

_Brian Kjersten, Paul McNamee_

- :fontawesome-solid-user-group: **Participant:** [hltcoe](./participants.md#hltcoe)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/hltcoe.kba.final.pdf](http://trec.nist.gov/pubs/trec21/papers/hltcoe.kba.final.pdf)
- :material-file-search: **Runs:** [hltcoe-wordNER500](./runs.md#hltcoe-wordner500) | [hltcoe-wordNER](./runs.md#hltcoe-wordner)

??? abstract "Abstract"
	
	Our team submitted runs for the TREC KBA Cumulative Citation Recommendation task. This task involves labeling over 300 million documents for whether they are relevant and/or central to particular entities already in a database. For this task, we used an SVM classifier that uses unigrams and named entities as binary features. In this paper, we describe our work for the 2012 evaluation and the results we obtained.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KjerstenM12.bib) "
	```
	@inproceedings{DBLP:conf/trec/KjerstenM12,
		author = {Brian Kjersten and Paul McNamee},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The {HLTCOE} Approach to the {TREC} 2012 {KBA} Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/hltcoe.kba.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KjerstenM12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### PRIS at TREC 2012 KBA Track

_Yan Li, Zhaozhao Wang, Baojin Yu, Yong Zhang, Ruiyang Luo, Weiran Xu, Guang Chen, Jun Guo_

- :fontawesome-solid-user-group: **Participant:** [PRIS](./participants.md#pris)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/PRIS.kba.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/PRIS.kba.nb.pdf)
- :material-file-search: **Runs:** [PRIS-PRIS_Run_1](./runs.md#pris-pris_run_1) | [PRIS-PRIS_Run_900](./runs.md#pris-pris_run_900) | [PRIS-PRIS_Run_800](./runs.md#pris-pris_run_800) | [PRIS-PRIS_Run_700](./runs.md#pris-pris_run_700) | [PRIS-PRIS_Run_600](./runs.md#pris-pris_run_600) | [PRIS-PRIS_Run_500](./runs.md#pris-pris_run_500) | [PRIS-PRIS_Run_400](./runs.md#pris-pris_run_400)

??? abstract "Abstract"
	
	Our system to KBA Track at TREC2012 is described in this paper, which includes preprocessing, index building, relevance feedback and similarity calculation. In particular, the Jaccard coefficient was applied to calculate the similarities between documents. We also show the evaluation results for our team and the comparison with the best and median evaluations.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiWYZLXCG12.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiWYZLXCG12,
		author = {Yan Li and Zhaozhao Wang and Baojin Yu and Yong Zhang and Ruiyang Luo and Weiran Xu and Guang Chen and Jun Guo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{PRIS} at {TREC} 2012 {KBA} Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/PRIS.kba.nb.pdf},
		timestamp = {Tue, 17 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiWYZLXCG12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Entity Profile Based Approach in Automatic Knowledge Finding

_Xitong Liu, Hui Fang_

- :fontawesome-solid-user-group: **Participant:** [udel_fang](./participants.md#udel_fang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/udel_fang.kba.nb.pdf](http://trec.nist.gov/pubs/trec21/papers/udel_fang.kba.nb.pdf)
- :material-file-search: **Runs:** [udel_fang-UDInfoKBA_EX](./runs.md#udel_fang-udinfokba_ex) | [udel_fang-UDInfoKBA_WIKI1](./runs.md#udel_fang-udinfokba_wiki1) | [udel_fang-UDInfoKBA_WIKI2](./runs.md#udel_fang-udinfokba_wiki2) | [udel_fang-UDInfoKBA_WIKI3](./runs.md#udel_fang-udinfokba_wiki3)

??? abstract "Abstract"
	
	We focus on the problem of profile building in this year's KBA track and proposed two methods. The first method is a baseline, which selects the stream items that has exact string match with the query entity. All the matched documents are assigned with the same relevance score. In the second method, we propose to use the related entities to help us identify the information related to the query entity. In particular, we retrieve the wikipedia pages for the query entities and extract the anchor text in all the internal links within the wikipedia page. These anchor text are treated as the related entities of the query entity and they are used to build the profile of the query entity. Given a stream item (i.e., a document), the relevance score is estimated by integrating the match with the query entity and the match with the related entities. Results on the training data show that the second method is more effective.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiuF12.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiuF12,
		author = {Xitong Liu and Hui Fang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Entity Profile Based Approach in Automatic Knowledge Finding},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/udel\_fang.kba.nb.pdf},
		timestamp = {Sun, 26 Feb 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiuF12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### SAWUS Siena's Automatic Wikipedia Update System

_Carl Tompkins, Zachary Witter, Sharon G. Small_

- :fontawesome-solid-user-group: **Participant:** [SCIATeam](./participants.md#sciateam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/SCIATeam.kba.final.pdf](http://trec.nist.gov/pubs/trec21/papers/SCIATeam.kba.final.pdf)

??? abstract "Abstract"
	
	The National Institute of Standards and Technology (NIST) has been running an annual Text Retrieval Competition and Conference (TREC) since 1992. This is a premier conference that offers researchers in the field of Computational Linguistics the opportunity to showcase their work and compare their results against other leading researchers. Our Siena research team participated in the TREC Knowledge Based Acquisition (KBA) Track, which was offered for the first time in 2012. The objective of this track is to drive research into automatic acquisition of knowledge, such as automatically updating Wikipedia by utilizing online news. Specifically our team of researchers developed a system that filters a stream of content for information that should be included on a given Wikipedia page. It was not yet clear how traditional Information Retrieval (IR) techniques perform for this task; therefore we began with a baseline test using current state of the art IR techniques. We then went on to experiment with query expansion, building a module that utilized Wikipedia Infoboxes to add terms to our query. This module was incorporated with our IR component to create SAWUS. Four submissions were sent to NIST to undergo a formal evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TompkinsWS12.bib) "
	```
	@inproceedings{DBLP:conf/trec/TompkinsWS12,
		author = {Carl Tompkins and Zachary Witter and Sharon G. Small},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{SAWUS} Siena's Automatic Wikipedia Update System},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/SCIATeam.kba.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TompkinsWS12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CWI at TREC 2012, KBA Track and Session Track

_Samur Araújo, Gebrekirstos G. Gebremeskel, Jiyin He, Corrado Boscarino, Arjen P. de Vries_

- :fontawesome-solid-user-group: **Participant:** [CWI](./participants.md#cwi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec21/papers/CWI.kba.session.final.pdf](http://trec.nist.gov/pubs/trec21/papers/CWI.kba.session.final.pdf)
- :material-file-search: **Runs:** [CWI-LEARNING16000](./runs.md#cwi-learning16000) | [CWI-DISAMBIGUATOR](./runs.md#cwi-disambiguator) | [CWI-LANGUAGEMODEL](./runs.md#cwi-languagemodel) | [CWI-google_dic_1](./runs.md#cwi-google_dic_1) | [CWI-google_dic_2](./runs.md#cwi-google_dic_2) | [CWI-google_dic_3](./runs.md#cwi-google_dic_3) | [CWI-google_strip_1](./runs.md#cwi-google_strip_1) | [CWI-google_strip_2](./runs.md#cwi-google_strip_2)

??? abstract "Abstract"
	
	We participated in two tracks: Knowledge Base Acceleration (KBA) Track and Session Track. In the KBA track, we focused on experimenting with different approaches as it is the first time the track is launched. We experimented with supervised and unsupervised retrieval models. Our supervised approach models include language models and a string-learning system. Our unsupervised approaches include using: 1)DBpedia labels and 2) Google-Cross-Lingual Dictionary (GCLD). While the approach that uses GCLD targets the central and relvant bins, all the rest target the central bin. The GCLD and the string-learning system have outperformed the others in their respective targeted bins. The goal of the Session track submission is to evaluate whether and how a logic framework for representing user interactions with an IR system can be used for improving the approximation of the relevant term distribution that another system that is supposed to have access to the session information will then calculate.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AraujoGHBV12.bib) "
	```
	@inproceedings{DBLP:conf/trec/AraujoGHBV12,
		author = {Samur Ara{\'{u}}jo and Gebrekirstos G. Gebremeskel and Jiyin He and Corrado Boscarino and Arjen P. de Vries},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{CWI} at {TREC} 2012, {KBA} Track and Session Track},
		booktitle = {Proceedings of The Twenty-First Text REtrieval Conference, {TREC} 2012, Gaithersburg, Maryland, USA, November 6-9, 2012},
		series = {{NIST} Special Publication},
		volume = {500-298},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2012},
		url = {http://trec.nist.gov/pubs/trec21/papers/CWI.kba.session.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AraujoGHBV12.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

