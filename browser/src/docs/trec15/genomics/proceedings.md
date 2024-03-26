# Proceedings - Genomics 2006 

#### TREC 2006 Genomics Track Overview

_William R. Hersh, Aaron M. Cohen, Phoebe M. Roberts, Hari Krishna Rekapalli_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/GEO06.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec15/papers/GEO06.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The TREC Genomics Track implemented a new task in 2006 that focused on passage retrieval for question answering using full-text documents from the biomedical literature. A test collection of 162,259 full-text documents and 28 topics expressed as questions was assembled. Systems were required to return passages that contained answers to the questions. Expert judges determined the relevance of passages and grouped them into aspects identified by one or more Medical Subject Headings (MeSH) terms. Document relevance was defined by the presence of one or more relevant aspects. The performance of submitted runs was scored using mean average precision (MAP) at the passage, aspect, and document level. In general, passage MAP was low, while aspect and document MAP were somewhat higher.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HershCRR06.bib) "
	```
	@inproceedings{DBLP:conf/trec/HershCRR06,
		author = {William R. Hersh and Aaron M. Cohen and Phoebe M. Roberts and Hari Krishna Rekapalli},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2006 Genomics Track Overview},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/GEO06.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HershCRR06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Report on the TREC 2006 Genomics Experiment

_Samir Abdou, Jacques Savoy_

- :fontawesome-solid-user-group: **Participant:** [uneuchatel.savoy](./participants.md#uneuchatel.savoy)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uneuchatel.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uneuchatel.geo.final.pdf)
- :material-file-search: **Runs:** [UniNE1](./runs.md#unine1) | [UniNE2](./runs.md#unine2) | [UniNE3](./runs.md#unine3)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC 2006 Genomics evaluation campaign. In an effort to find text passages that will meet user requests, we propose and evaluate a new approach to the generation of orthographic variants of search terms (mainly genomic names in our case). We also evaluate the retrieval effectiveness of both the Okapi (BM25) model and the I(n)B2 probabilistic model derived from the Divergence from Randomness paradigm. In our experiments, we find that in terms of mean average precision the latter model performs clearly better than the Okapi model (with a relative difference of 50%). Moreover when comparing a 5-gram indexing approach to word-based indexing schemes, the mean average precision decreases by about 10% when using the n-gram indexing scheme. Additionally, including the article's title in all passages generated from a given article does not improve retrieval effectiveness. Finally, the generation of passages delimited by HTML tags was not a success. The performance achieved was in fact rather poor, suggesting that there were too many sentences within such text passages.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AbdouS06.bib) "
	```
	@inproceedings{DBLP:conf/trec/AbdouS06,
		author = {Samir Abdou and Jacques Savoy},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Report on the {TREC} 2006 Genomics Experiment},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uneuchatel.geo.final.pdf},
		timestamp = {Wed, 07 Jul 2021 16:44:22 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AbdouS06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BioKI, A General Literature Navigation System at TREC Genomics  2006

_Sabine Bergler, Jonathan Schuman, Julien Dubuc, Alexandr Lebedev_

- :fontawesome-solid-user-group: **Participant:** [concordiau.bergler](./participants.md#concordiau.bergler)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/concordiau.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/concordiau.geo.final.pdf)
- :material-file-search: **Runs:** [BioKI1](./runs.md#bioki1) | [BioKI2](./runs.md#bioki2) | [BioKI3](./runs.md#bioki3)

??? abstract "Abstract"
	
	We present the passage reranking component of a general literature navigation system. Based on weighted keyword scoring without automatic enhancements such as term expansion, the system performed slightly above average on all three tasks, with a strong performance on aspect retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BerglerSDL06.bib) "
	```
	@inproceedings{DBLP:conf/trec/BerglerSDL06,
		author = {Sabine Bergler and Jonathan Schuman and Julien Dubuc and Alexandr Lebedev},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {BioKI, {A} General Literature Navigation System at {TREC} Genomics 2006},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/concordiau.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BerglerSDL06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Concept Recognition, Information Retrieval, and Machine Learning in  Genomics Question-Answering

_J. Gregory Caporaso, William A. Baumgartner Jr., Hyunmin Kim, Zhiyong Lu, Helen L. Johnson, Olga Medvedeva, Anna Lindemann, Lynne M. Fox, Elizabeth K. White, K. Bretonnel Cohen, Lawrence Hunter_

- :fontawesome-solid-user-group: **Participant:** [ucolorado.cohen](./participants.md#ucolorado.cohen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/ucolorado.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/ucolorado.geo.final.pdf)
- :material-file-search: **Runs:** [uchsc1](./runs.md#uchsc1) | [uchsc2](./runs.md#uchsc2) | [uchsc3](./runs.md#uchsc3)

??? abstract "Abstract"
	
	TREC Genomics 2006 presented a genomics question-answering challenge with questions on twenty-seven topics, and a corpus of 162,259 full-text biomedical journal articles from which to derive answers. Questions were formulated from actual information needs of biomedical researchers, and performance was based on human evaluation of the answers. The University of Colorado approach to this task involved three key components: semantic analysis, document zoning, and a promiscuous retrieval approach followed by pruning by classifiers trained to identify near-misses. We began by parsing the document HTML, splitting it into paragraph-length passages and classifying each passage with respect to a model of the sections (zones) of scientific publications. We filtered out certain sections, and built a search index for these passages using the Lemur system. Next, for each query, we semi-automatically created a set of expansions using ontological resources, including MeSH and the Gene Ontology. This expansion included not only synonyms, but terms related to concepts that were both more specific and (in some cases) more general than the query. We searched the passage collection for these expanded queries using the Indri search engine from the Lemur package, with pseudo-relevance feedback. We also tried expanding the retrieved passages by adding passages that had a small cosine distance to the initial retrievals in an LSA-defined vector space. Our final step was to filter this expanded retrieval set with document classifiers whose input features included word stems and recognized concepts. Three separate runs were constructed using varying components of the above set, allowing us to explore the utility of each. The system produced the best result for at least one query in each of the three evaluations (document, passage and aspect diversity).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CaporasoBKLJMLFWCH06.bib) "
	```
	@inproceedings{DBLP:conf/trec/CaporasoBKLJMLFWCH06,
		author = {J. Gregory Caporaso and William A. Baumgartner Jr. and Hyunmin Kim and Zhiyong Lu and Helen L. Johnson and Olga Medvedeva and Anna Lindemann and Lynne M. Fox and Elizabeth K. White and K. Bretonnel Cohen and Lawrence Hunter},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Concept Recognition, Information Retrieval, and Machine Learning in Genomics Question-Answering},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/ucolorado.geo.final.pdf},
		timestamp = {Tue, 26 Jan 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CaporasoBKLJMLFWCH06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Combining Lexicon Expansion, Information Retrieval, and Cluster-based  Ranking for Biomedical Question Answering

_Aaron M. Cohen, Jianji Yang, Seeger Fisher, Brian Roark, William R. Hersh_

- :fontawesome-solid-user-group: **Participant:** [ohsu.hersh](./participants.md#ohsu.hersh)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/ohsu.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/ohsu.geo.final.pdf)
- :material-file-search: **Runs:** [OHSUNoclu](./runs.md#ohsunoclu) | [OHSUCluster](./runs.md#ohsucluster) | [OHSUBigclu](./runs.md#ohsubigclu)

??? abstract "Abstract"
	
	The Oregon Health & Science University submission to the TREC 2006 Genomics Track approached the question answer extraction task in three phases. In the first phase the biological questions were parsed into relevant entities and query expressions were generated. The second phase retrieved relevant passages from the corpus using Lucene as an information retrieval engine. The third phase performed ranking of the retrieved passages and generated the final submitted output. Through these experiments and comparison with the approaches of others we hope to learn the contribution and value of several techniques applicable to question answer extraction including: lexicon-based query term expansion, query back-off techniques for questions with few applicable passages, and passage clustering for identifying distinct aspects of question answers. Our experiments showed no improvement after cluster-based ranking. Maximal span based passage indexing proved to be too coarse, resulting in an overall average performing passage MAP of 4%.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CohenYFRH06.bib) "
	```
	@inproceedings{DBLP:conf/trec/CohenYFRH06,
		author = {Aaron M. Cohen and Jianji Yang and Seeger Fisher and Brian Roark and William R. Hersh},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Combining Lexicon Expansion, Information Retrieval, and Cluster-based Ranking for Biomedical Question Answering},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/ohsu.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CohenYFRH06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Finding Relevant Passages in Scientific Articles: Fusion of Automatic  Approaches vs. an Interactive Team Effort

_Dina Demner-Fushman, Susanne M. Humphrey, Nicholas C. Ide, Russell F. Loane, Patrick Ruch, Miguel E. Ruiz, Lawrence H. Smith, Lorraine K. Tanabe, W. John Wilbur, Alan R. Aronson_

- :fontawesome-solid-user-group: **Participant:** [nlm.aronson](./participants.md#nlm.aronson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/nlm.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/nlm.geo.final.pdf)
- :material-file-search: **Runs:** [NLMinter](./runs.md#nlminter) | [NLMfusion](./runs.md#nlmfusion) | [NLMmanual](./runs.md#nlmmanual)

??? abstract "Abstract"
	
	This paper presents our approach to retargeting the information retrieval systems designed and/or optimized for retrieval of MEDLINE citations to the task of finding relevant passages in the text of scientific articles. To continue using our TREC 2005 fusion approach, we needed a common representation for the full text biomedical articles to be shared by the four base systems (Essie, SMART, EasyIR and Theme.) The base systems relied upon previously developed NLP, statistical and ML methods. The fusion of the automatic runs improved the results of three contributing base systems at 99.9% significance level on all metrics: document, passage, and aspect precision. The fusion run outperformed Essie, the best of the base systems, at 94% to 99% significance level, with the exception of passage precision. The novelty of the task and the lack of training data inspired our exploration of an interactive approach. The prohibitive cost (in time and domain expert effort) required for a truly interactive retrieval led to a team interaction with one of the base systems - Essie. The initial queries were developed by a computational biologist and a medical librarian. The librarian merged and then refined the queries upon inspecting the initial search results. The refined queries were submitted as a batch without further interaction with the system. The interactive results, the best we achieved, improved over the baseline automatic Essie run at the 91% significance level. The difference between the fusion and the interactive results is not statistically significant.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Demner-FushmanHILSTWADRR06.bib) "
	```
	@inproceedings{DBLP:conf/trec/Demner-FushmanHILSTWADRR06,
		author = {Dina Demner{-}Fushman and Susanne M. Humphrey and Nicholas C. Ide and Russell F. Loane and Patrick Ruch and Miguel E. Ruiz and Lawrence H. Smith and Lorraine K. Tanabe and W. John Wilbur and Alan R. Aronson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Finding Relevant Passages in Scientific Articles: Fusion of Automatic Approaches vs. an Interactive Team Effort},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/nlm.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Demner-FushmanHILSTWADRR06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BioText Team Report for the TREC 2006 Genomics Track

_Anna Divoli, Marti A. Hearst, Preslav Nakov, Ariel S. Schwartz_

- :fontawesome-solid-user-group: **Participant:** [ucal-berkeley.larso](./participants.md#ucal-berkeley.larso)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/ucalifornia-berkeley.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/ucalifornia-berkeley.geo.final.pdf)
- :material-file-search: **Runs:** [biotext1](./runs.md#biotext1) | [biotextweb](./runs.md#biotextweb) | [biotext3](./runs.md#biotext3)

??? abstract "Abstract"
	
	The paper reports on the work conducted by the BioText team at UC Berkeley for the TREC 2006 Genomics track. Our approach had three main focal points: First, based on our successful results in the TREC 2003 Genomics track [1], we emphasized gene name recall. Second, given the structured nature of the Generic Topic Types (GTTs), we attempted to design queries that covered every part of the topics, including synonym expansion. Third, inspired by having access to the full text of documents, we experimented with identifying and weighting information depending on which section (Introduction, Results, etc.) it appeared in. Our emphasis on covering the different pieces of the query may have helped with the aspects ranking portion of the task, as we performed best on that evaluation measure. We submitted three runs: Biotext1, BiotextWeb, and Biotext3. All runs were fully automatic. The Biotext1 run performed best, achieving MAP scores of .24 on aspects, .35 on documents, and .035 on passages.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DivoliHNS06.bib) "
	```
	@inproceedings{DBLP:conf/trec/DivoliHNS06,
		author = {Anna Divoli and Marti A. Hearst and Preslav Nakov and Ariel S. Schwartz},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {BioText Team Report for the {TREC} 2006 Genomics Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/ucalifornia-berkeley.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DivoliHNS06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Twease at TREC 2006: Breaking and Fixing BM25 Scoring With Query  Expansion, A Biologically Inspired Double Mutant Recovery Experiment

_Kevin C. Dorff, Matthew J. Wood, Fabien Campagne_

- :fontawesome-solid-user-group: **Participant:** [weill-med-cornellu](./participants.md#weill-med-cornellu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/weill-cornell.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/weill-cornell.geo.final.pdf)
- :material-file-search: **Runs:** [icb1](./runs.md#icb1) | [icb2](./runs.md#icb2) | [icb3](./runs.md#icb3)

??? abstract "Abstract"
	
	This is the first year that our group has participated in the genomics track of TREC. We enter the evaluation with a new biomedical search engine, developed as an open-source project which relies heavily on MG4J, and is publicly available at http://www.twease.org. We designed our runs to test the features of Twease that most distinguish it from other biomedical search engines. Such features include: (1) a custom biomedical query expansion module (which draws on biomedical thesauri, but also includes a statistical model of morphological word variations observed in the biomedical domain); (2) the ability to search the index simultaneously at the whole document level, or at the sentence level. Our official runs evaluated the performance of minimal interval semantics when used with custom morphological word expansion on a biomedical corpus. Our best official run scored MAP=0.30 at the document level, slightly above the median of other submissions. Our non-official runs compared minimal interval semantics to BM25 on the same topics and corpus. We varied the level of query expansion for both methods, and demonstrated how easily BM25 breaks down as more related terms are added to a query, while minimal interval semantics is robust to such change. We investigated the origin of the issue with a biologically inspired experimental design (mutation recovery). Our results help understand why certain groups observe performance drops with thesaurus-based query expansion, while other groups report the opposite effect. The best of our non-official runs achieves a MAP document level of 0.32 when an intermediate level of query expansion is used. This manuscript also describes our first attempt at passage retrieval in full text articles (we achieved a MAP of 0.052, above the median of 0.028).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DorffWC06.bib) "
	```
	@inproceedings{DBLP:conf/trec/DorffWC06,
		author = {Kevin C. Dorff and Matthew J. Wood and Fabien Campagne},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Twease at {TREC} 2006: Breaking and Fixing {BM25} Scoring With Query Expansion, {A} Biologically Inspired Double Mutant Recovery Experiment},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/weill-cornell.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DorffWC06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Extraction of Document Structure for Genomics Documents

_David Eichmann_

- :fontawesome-solid-user-group: **Participant:** [uiowa.eichmann](./participants.md#uiowa.eichmann)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uiowa.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uiowa.geo.final.pdf)
- :material-file-search: **Runs:** [UIowa06Geno1](./runs.md#uiowa06geno1) | [UIowa06Geno2](./runs.md#uiowa06geno2) | [UIowa06Geno3](./runs.md#uiowa06geno3)

??? abstract "Abstract"
	
	The University of Iowa participated only in the genomics track in TREC-2006. Our work concentrated almost entirely on exploring how accurately we could regenerate the logical structure of each of the documents in the corpus from their HTML instantiations. This year's work is hence primarily infrastructure building, with little in the way of support for the track's specific tasks in place.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Eichmann06.bib) "
	```
	@inproceedings{DBLP:conf/trec/Eichmann06,
		author = {David Eichmann},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Extraction of Document Structure for Genomics Documents},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uiowa.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Eichmann06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Ranking Biomedical Passages for Relevance and Diversity: University  of Wisconsin, Madison at TREC Genomics 2006

_Andrew B. Goldberg, David Andrzejewski, Jurgen Van Gael, Burr Settles, Xiaojin Zhu, Mark Craven_

- :fontawesome-solid-user-group: **Participant:** [uwisconsin.craven](./participants.md#uwisconsin.craven)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uwisconsin.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uwisconsin.geo.final.pdf)
- :material-file-search: **Runs:** [WiscRun1](./runs.md#wiscrun1) | [WiscRun2](./runs.md#wiscrun2) | [WiscRun3](./runs.md#wiscrun3)

??? abstract "Abstract"
	
	We report on the University of Wisconsin, Madison's experience in the TREC Genomics 2006 track, which asks participants to retrieve passages from scientific articles that satisfy biologists' information needs. An emphasis is placed on returning relevant passages that discuss different aspects of the topic. Using an off-the-shelf information retrieval (IR) engine, we focused on query generation and reranking query results to encourage relevance and diversity. For query generation, we automatically identify noun phrases from the topic descriptions, and use online resources to gather synonyms as expansion terms. Our first submission uses the baseline IR engine results. We rerank the passages using a na¨ıve clustering-based approach in our second run, and we test GRASSHOPPER , a novel graph-theoretic algorithm based on absorbing random walks, in our third run. While our aspect-level results appear to compare favorably with other participants' on average, our query generation techniques failed to produce adequate query results for several topics, causing our passage and document-level evaluation scores to suffer. Furthermore, we surprisingly achieved higher aspect-level scores using the initial ranking than our methods aimed specifically at promoting diversity. While this sounds discouraging, we have several ideas as to why this happened and hope to produce new methods that correct these shortcomings.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GoldbergAGSZC06.bib) "
	```
	@inproceedings{DBLP:conf/trec/GoldbergAGSZC06,
		author = {Andrew B. Goldberg and David Andrzejewski and Jurgen Van Gael and Burr Settles and Xiaojin Zhu and Mark Craven},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Ranking Biomedical Passages for Relevance and Diversity: University of Wisconsin, Madison at {TREC} Genomics 2006},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uwisconsin.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GoldbergAGSZC06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2006: Genomics Track

_Xiangji Huang, Bin Hu, Hashmat Rohian_

- :fontawesome-solid-user-group: **Participant:** [yorku.huang](./participants.md#yorku.huang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/yorku.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/yorku.geo.final.pdf)
- :material-file-search: **Runs:** [york06ga1](./runs.md#york06ga1) | [york06ga3](./runs.md#york06ga3) | [york06ga4](./runs.md#york06ga4)

??? abstract "Abstract"
	
	Our Genomics experiments mainly focus on addressing four problems in biomedical information retrieval. The four problems are: (1) how to deal with synonyms? (2) how to deal with the frequent use of acronyms? (3) how to deal with homonyms? (4) how to deal with the document-level retrieval, passage-level retrieval and aspect-level retrieval? In particular, we use the automatic query expansion algorithm proposed at TREC 2005 to construct structured queries for document-level retrieval and we also apply several data mining techniques for passage-level retrieval and aspect-level retrieval. The mean average precisions (MAP) for our automatic run “york06ga1” are 0.3365 at the document-level retrieval, 0.0197 at the passage-level retrieval and 0.1084 at the aspect-level retrieval. The evaluation results show that the automatic query expansion algorithm is effective for improving document-level retrieval performance. However, our retrieval performance on passage-level and aspect-level is poor. One possible reason is that we did not follow the TREC 2006 Genomics track protocol regarding the calculation of passage measures correctly. Therefore, we built a completely wrong index for the passage-level retrieval. Since our aspect-level retrieval is based on the results obtained from our passage level retrieval, the results thus obtained are sub-optimal.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HuangHR06.bib) "
	```
	@inproceedings{DBLP:conf/trec/HuangHR06,
		author = {Xiangji Huang and Bin Hu and Hashmat Rohian},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {York University at {TREC} 2006: Genomics Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/yorku.geo.final.pdf},
		timestamp = {Sun, 02 Oct 2022 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HuangHR06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Robust Pseudo Feedback Estimation and HMM Passage Extraction: UIUC  at TREC 2006 Genomics Track

_Jing Jiang, Xin He, ChengXiang Zhai_

- :fontawesome-solid-user-group: **Participant:** [uillinois.chicago.zhou](./participants.md#uillinois.chicago.zhou)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uillinois-uc.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uillinois-uc.geo.final.pdf)
- :material-file-search: **Runs:** [UICGenRun1](./runs.md#uicgenrun1) | [UICGenRun2](./runs.md#uicgenrun2) | [UICGenRun3](./runs.md#uicgenrun3)

??? abstract "Abstract"
	
	The University of Illinois at Urbana-Champaign (UIUC) participated in TREC 2006 Genomics Track. Our focus this year was to apply two language modeling techniques for information retrieval that have been proposed recently by our group [4, 1]. These two techniques have been shown to be effective for general English text. It is not clear, though, how they perform on text in special domains such as the biomedical domain. We therefore tested their effectiveness for this year's genomics task. First, we tried to improve the pseudo relevance feedback mechanism in the retrieval model by applying a recently proposed regularized estimation method [4]. In the KL-divergence retrieval framework, pseudo relevance feedback documents can be used to better estimate the query model [5]. While in the original proposed method [5], this estimation involved two parameters that need to be empirically set, recent work showed that a more robust, regularized estimation method that involves less parameter tuning can be effective [4]. We therefore applied this estimation method to this year's genomics task to see whether it can improve the pseudo relevance feedback mechanism in biomedical information retrieval as well. Second, since this year's task is defined as passage retrieval rather than document retrieval, a challenge is how to extract coherent and relevant passages from whole documents. Previously, we proposed a hidden Markov model (HMM)-based passage extraction method that was shown to be effective in the general English domain [1]. We applied this method to this year's genomics task to see whether this method is also effective for biomedical text. Besides the two language modeling techniques, we also tested the use of user relevance feedback for retrieval, to see how much human interaction can help improve the performance. We obtained some manual judgments from two domain experts, and used them in the two interactive runs Our experiment results showed that the regularized estimation method for pseudo relevance feedback performed similarly to the original estimation method when both methods were under the optimal parameter setting, and outperformed the original estimation method when both methods were under the default parameter setting. Because in reality we do not know the optimal parameter setting, the regularized estimation method is thus more robust than the original estimation method. Our experiment results also showed that the HMM-based passage extraction method outperformed a baseline method that returns whole paragraphs as passages. However, our HMM-based passage extraction method tends to return relatively long and coherent passages, which may not be optimal for the genomics task this year, because in this task the information need is more specific. Finally, our experiment results showed that user relevance feedback was very effective, as we expected.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/JiangHZ06.bib) "
	```
	@inproceedings{DBLP:conf/trec/JiangHZ06,
		author = {Jing Jiang and Xin He and ChengXiang Zhai},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Robust Pseudo Feedback Estimation and {HMM} Passage Extraction: {UIUC} at {TREC} 2006 Genomics Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uillinois-uc.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/JiangHZ06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### NTU at TREC 2006 Genomics Track

_Kevin Hsin-Yih Lin, Wen-Juan Hou, Hsin-Hsi Chen_

- :fontawesome-solid-user-group: **Participant:** [ntu.chen](./participants.md#ntu.chen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/ntu.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/ntu.geo.final.pdf)
- :material-file-search: **Runs:** [NTUadh1](./runs.md#ntuadh1) | [NTUadh2](./runs.md#ntuadh2) | [NTUadh3](./runs.md#ntuadh3)

??? abstract "Abstract"
	
	In this paper, we present a system for information retrieval of biomedical texts at passage level. Our system used KL-divergence as the underlying retrieval model. We further added query expansion and performed post-processing on the results. We were able to obtain a Document MAP of 0.3563, Passage MAP of 0.0464 and Aspect MAP of 0.2255 on one of the three runs.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinHC06.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinHC06,
		author = {Kevin Hsin{-}Yih Lin and Wen{-}Juan Hou and Hsin{-}Hsi Chen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{NTU} at {TREC} 2006 Genomics Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/ntu.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LinHC06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Expanding Queries Using Multiple Resources

_Edgar Meij, Maarten de Rijke, Machiel Jansen_

- :fontawesome-solid-user-group: **Participant:** [uamsterdam.meij](./participants.md#uamsterdam.meij)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uamsterdam-meij.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uamsterdam-meij.geo.final.pdf)
- :material-file-search: **Runs:** [UAmsBaseLine](./runs.md#uamsbaseline) | [UAmsExp](./runs.md#uamsexp) | [UAmsExpSel](./runs.md#uamsexpsel)

??? abstract "Abstract"
	
	We describe our participation in the TREC 2006 Genomics track, in which our main focus was on query expansion. We hypothesized that applying query expansion techniques would help us both to identify and retrieve synonymous terms, and to cope with ambiguity. To this end, we developed several collection-specific as well as web-based strategies. We also performed post-submission experiments, in which we compare various retrieval engines, such as Lucene, Indri, and Lemur, using a simple baseline topic-set. When indexing entire paragraphs as pseudo-documents, we find that Lemur is able to achieve the highest document-, passage-, and aspect-level scores, using the KL-divergence method and its default settings. Additionally, we index the collection at a lower level of granularity, by creating pseudo-documents comprising of individual sentences. When we search these instead of paragraphs in Lucene, the passage-level scores improve considerably. Finally we note that stemming improves overall scores by at least 10%.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MeijRJ06.bib) "
	```
	@inproceedings{DBLP:conf/trec/MeijRJ06,
		author = {Edgar Meij and Maarten de Rijke and Machiel Jansen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Expanding Queries Using Multiple Resources},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uamsterdam-meij.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MeijRJ06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Report on the TREC 2006 Experiment: Genomics Track

_Patrick Ruch, Frédéric Ehrler, Julien Gobeill, Imad Tbahriti, Antonio Jimeno-Yepes_

- :fontawesome-solid-user-group: **Participant:** [uhosp-geneva.ruch](./participants.md#uhosp-geneva.ruch)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uhosp-geneva.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uhosp-geneva.geo.final.pdf)
- :material-file-search: **Runs:** [UnigeGO](./runs.md#unigego) | [UnigeMesh](./runs.md#unigemesh) | [UniGe](./runs.md#unige)

??? abstract "Abstract"
	
	In previous TREC Genomics competition, ad hoc experiments were based on MEDLINE corpora (about 4.5 millions in 2005). This year, the collection has been replaced by a collection of about 160000 full-text articles. The proposed task is a passage retrieval task. Because document length in MEDLINE follow a binomial distribution (Figure 1), our previous investigations were focused on exploring the document length parameter, using a slightly modified pivoted normalization factor (Singhal 1999, Fujita 2004). This year, our efforts concentrated on combining knowledge-driven methods to a standard vector-space retrieval system.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RuchEGTY06.bib) "
	```
	@inproceedings{DBLP:conf/trec/RuchEGTY06,
		author = {Patrick Ruch and Fr{\'{e}}d{\'{e}}ric Ehrler and Julien Gobeill and Imad Tbahriti and Antonio Jimeno{-}Yepes},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Report on the {TREC} 2006 Experiment: Genomics Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uhosp-geneva.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RuchEGTY06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UB at TREC Genomics 2006: Using Passage Retrieval and Pre-Retrieval  Query Expansion for Genomics IR

_Miguel E. Ruiz_

- :fontawesome-solid-user-group: **Participant:** [suny-buffalo.ruiz](./participants.md#suny-buffalo.ruiz)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/suny-buffalo.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/suny-buffalo.geo.final.pdf)
- :material-file-search: **Runs:** [UBexp1](./runs.md#ubexp1) | [UBexp2](./runs.md#ubexp2) | [UBexp1M](./runs.md#ubexp1m) | [UBexp2M](./runs.md#ubexp2m)

??? abstract "Abstract"
	
	This paper presents the results of the University at Buffalo (UB) in TREC genomics. For this task we used the SMART retrieval system and a pre retrieval expansion method that uses the ABGene and MetaMap tools. We tried two different weighting schemes one using pivoted length normalization (Lnu.ltu) and another using augmented tf-idf (atn.ann). The results show that performance of pivoted length normalization is very close to the median system that participated in the Genomics track. The augmented tf-idf performs significantly above the median system showing an improvement of 21%. This seems to indicate that a simpler weighting scheme could work better for retrieval of relevant passages.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Ruiz06.bib) "
	```
	@inproceedings{DBLP:conf/trec/Ruiz06,
		author = {Miguel E. Ruiz},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UB} at {TREC} Genomics 2006: Using Passage Retrieval and Pre-Retrieval Query Expansion for Genomics {IR}},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/suny-buffalo.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Ruiz06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Combining Multiple Resources, Evidences and Criteria for Genomic Information  Retrieval

_Luo Si, Jie Lu, Jamie Callan_

- :fontawesome-solid-user-group: **Participant:** [purdueu.si](./participants.md#purdueu.si)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/purdue-cmu.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/purdue-cmu.geo.final.pdf)
- :material-file-search: **Runs:** [PCPsgRescore](./runs.md#pcpsgrescore) | [PCPsgClean](./runs.md#pcpsgclean) | [PCPsgAspect](./runs.md#pcpsgaspect)

??? abstract "Abstract"
	
	We participated in the passage retrieval and aspect retrieval subtasks of the TREC 2006 Genomics Track. This paper describes the methods developed for these two subtasks. For passage retrieval, our query expansion method utilizes multiple external biomedical resources to extract acronyms, aliases, and synonyms, and we propose a post-processing step which combines the evidence from multiple scoring methods to improve relevance-based passage rankings. For aspect retrieval, our method estimates the topical aspects of the retrieved passages and generates passage rankings by considering both topical relevance and topical novelty. Empirical results demonstrate the effectiveness of these methods.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SiLC06.bib) "
	```
	@inproceedings{DBLP:conf/trec/SiLC06,
		author = {Luo Si and Jie Lu and Jamie Callan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Combining Multiple Resources, Evidences and Criteria for Genomic Information Retrieval},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/purdue-cmu.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SiLC06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UMass Genomics 2006: Query-Biased Pseudo Relevance Feedback

_Mark D. Smucker_

- :fontawesome-solid-user-group: **Participant:** [umass.allan](./participants.md#umass.allan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/umass.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/umass.geo.final.pdf)
- :material-file-search: **Runs:** [UMassCIIR1](./runs.md#umassciir1) | [UMassCIIR2](./runs.md#umassciir2) | [UMassCIIR1L](./runs.md#umassciir1l)

??? abstract "Abstract"
	
	Query-biased pseudo relevance feedback creates document representations for document feedback that aim to be more relevant to the user than using the entire document. Our submitted runs using query-biased feedback degraded performance compared to not using feedback. The cause of this degradation was the use of too many documents for feedback. Preliminary document retrieval experiments using fewer feedback documents found that query-biasing produced gains in the geometric mean average precision that non-biased feedback did not produce.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Smucker06.bib) "
	```
	@inproceedings{DBLP:conf/trec/Smucker06,
		author = {Mark D. Smucker},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {UMass Genomics 2006: Query-Biased Pseudo Relevance Feedback},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/umass.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Smucker06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Passage Retrieval by Shrinkage of Language Models

_Fei Song, Joe Vasak, Wei Wang_

- :fontawesome-solid-user-group: **Participant:** [uguelph.song](./participants.md#uguelph.song)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uguelph.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uguelph.geo.final.pdf)
- :material-file-search: **Runs:** [UofG2](./runs.md#uofg2) | [UofG1](./runs.md#uofg1) | [UofG0](./runs.md#uofg0)

??? abstract "Abstract"
	
	Information retrieval is the process of searching for relevant documents that satisfy a user's information need (usually in the form of queries). Some of its successful applications include library catalogue search, medical record retrieval, and Internet search engines (e.g., Google). As the exponential growth of web pages and online documents continues, there is an increasing need for retrieval systems that are capable of dealing with a large collection of documents and at the same time narrowing the scope of the search results (not only relevant documents but also relevant passages or even direct answers). A number of conceptual models have been proposed for information retrieval, including the Boolean model [Baeza-Yates and Ribeiro-Neto, 1999], the vector-space model [Salton, 1989], probabilistic models [Robertson and Sparck Jones, 1976], the inference network model [Croft and Turtle, 1992], and the language models [Ponte and Croft, 1998; Hiemstra, 1998; Miller et al., 1999]. Among these models, language models have recently received a lot of attention in the field of information retrieval, since they are based on the solid foundation of statistical natural language processing and are both intuitive and flexible for extensions with more features to handle the retrieval tasks. In language modeling, we view each document as a language sample and estimate the probabilities of producing individual terms in a document. A query is treated as a generation process. Given a sequence of terms in a query, we compute the probabilities of generating these terms according to each document model. The multiplication of these probabilities is then used to rank the retrieved documents: the higher the generation probabilities, the more relevant the corresponding documents to the given query. One big obstacle in applying language modeling to information retrieval is the sparse data problem. Unlike a collection of documents where we can control the number of documents in it, a document itself is often small in size and its content is always fixed. Even for a relatively long document, some of the words can still be rare or missing according to the Zipf's law of language usage [Manning and Schütze, 1999]. As a result, the combination of individual probabilities through multiplications will be meaningless if one of the probabilities is zero (for a missing term in a document). Thus, overcoming the sparse data problem is the key for the success of any language modeling system for information retrieval.  For TREC 2006 Genomics Track (see http://ir.ohsu.edu/genomics/ for more information), the data set presents several new challenges for language modeling in specific and information retrieval in general. First of all, the search is targeted to the relevant passages within documents (more or less corresponding to paragraphs), since users of the biomedical domain are likely interested in finding answers along with the context that provides supporting information and links to the original sources. Secondly, there is a need to balance the results across different documents and aspects. An aspect is defined as a group of passages of similar content, which will be judged by human evaluators and identified by a set of MeSH terms for the Genomics data set. By ensuring an adequate coverage of the results across documents and aspects, we can reduce the repeats (or duplicate passages) and maintain a reasonable number of novel/unique passages, which may be particularly useful for biomedical researchers. Finally, the retrieved passages may need to be trimmed further to highlight the answers, since passages are typically organized as paragraphs and may contain irrelevant wording before and after the relevant answers. In the rest of the working note, we describe our retrieval method based on the language models and their combinations in section 2. In section 3, we explain the enhancements for balancing the results for documents and aspects and narrowing the spans for the answers in the retrieved passages. In section 4, we discuss our experimental results on the Genomics data set. Finally, we conclude and point future directions of our work in section 5.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SongVW06.bib) "
	```
	@inproceedings{DBLP:conf/trec/SongVW06,
		author = {Fei Song and Joe Vasak and Wei Wang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Passage Retrieval by Shrinkage of Language Models},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uguelph.geo.final.pdf},
		timestamp = {Wed, 12 Apr 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/SongVW06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### ASU at TREC 2006 Genomics Track

_Luis Tari, Graciela Gonzalez, Robert Leaman, Shawn Nikkila, Ryan Wendt, Chitta Baral_

- :fontawesome-solid-user-group: **Participant:** [arizona-stateu.gonzalez](./participants.md#arizona-stateu.gonzalez)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/arizona-su.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/arizona-su.geo.final.pdf)
- :material-file-search: **Runs:** [asubaral](./runs.md#asubaral) | [asubaral2](./runs.md#asubaral2) | [asubaral3](./runs.md#asubaral3)

??? abstract "Abstract"
	
	This paper describes our experiments in the TREC 2006 Genomics track submitted by the ASU BioAI group, as well as experiments based on the improvements made after our submission. Some of the major issues we tried to address in our experiments are how to (1) extract keywords from natural language questions in the biomedical domain and (2) determine the relevancy of passages
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TariGLNWB06.bib) "
	```
	@inproceedings{DBLP:conf/trec/TariGLNWB06,
		author = {Luis Tari and Graciela Gonzalez and Robert Leaman and Shawn Nikkila and Ryan Wendt and Chitta Baral},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{ASU} at {TREC} 2006 Genomics Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/arizona-su.geo.final.pdf},
		timestamp = {Wed, 25 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TariGLNWB06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Concept Based Document Retrieval for Genomics Literature

_Dolf Trieschnigg, Wessel Kraaij, Martijn J. Schuemie_

- :fontawesome-solid-user-group: **Participant:** [erasmus.schuemie](./participants.md#erasmus.schuemie)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/erasmus-tno-utwente.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/erasmus-tno-utwente.geo.final.pdf)
- :material-file-search: **Runs:** [EMCUT1](./runs.md#emcut1) | [EMCUT2](./runs.md#emcut2)

??? abstract "Abstract"
	
	The 2006 TREC Genomics evaluation focuses on document, passage and aspect retrieval in the genomics domain. The Erasmus Medical Center, TNO and University of Twente collaborated on an approach combining concept tagging (named entity recognition) and information retrieval based on statistical language models. Experiments on the 2004 collection show that document retrieval based on concepts could not outperform the baseline based on words. However, experiments on the 2006 collection shows no significant difference between the two approaches. Further investigation has to show if and how these concept and word based language models can be effectively combined.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TrieschniggKS06.bib) "
	```
	@inproceedings{DBLP:conf/trec/TrieschniggKS06,
		author = {Dolf Trieschnigg and Wessel Kraaij and Martijn J. Schuemie},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Concept Based Document Retrieval for Genomics Literature},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/erasmus-tno-utwente.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TrieschniggKS06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IIT TREC 2006: Genomics Track

_Jay Urbain, Nazli Goharian, Ophir Frieder_

- :fontawesome-solid-user-group: **Participant:** [iit.urbain](./participants.md#iit.urbain)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/iit.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/iit.geo.final.pdf)
- :material-file-search: **Runs:** [iitx1](./runs.md#iitx1) | [iitx2](./runs.md#iitx2) | [iitx3](./runs.md#iitx3)

??? abstract "Abstract"
	
	For the TREC-2006 Genomics Track, we report on the effectiveness of composite information retrieval functions based on a dimensional data model for improving document, passage, and aspect search precision of genomics literature. We designed an approach, and developed a corresponding search engine, based on a novel dimensional data model capable of document, paragraph, sentence, and passage level retrieval of genomics literature. By constructing a data warehouse style index with the flexibility of aggregating term statistics at multiple levels of document granularity, and incorporating key biological entities through shallow parsing of individual sentences, composite retrieval models combining multiple levels of contextual evidence can be efficiently developed to improve retrieval performance. The genomics track for 2006 measured document, passage, and aspect retrieval using 27 topics created by active biological researchers. Each topic fit within one of four question-oriented topic templates: the role of a gene in a disease, the effect of a gene on a biological process, how genes interact in organ function, and how mutations in genes influence biological processes. Documents for this task come from a corpus of 162,048 full-text biomedical articles. Each form of retrieval was measured with a variant of mean average precision (MAP). We submitted automatically generated results from three composite models to the TREC forum. All three models delivered results that significantly exceed the median results reported for the 2006 TREC Genomics track. The results of our best performing TREC model had MAP of 0.426 for document retrieval (53% above median), 0.055 for passage retrieval (129% above median), and 0.262 for aspect retrieval (125% above median).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/UrbainGF06.bib) "
	```
	@inproceedings{DBLP:conf/trec/UrbainGF06,
		author = {Jay Urbain and Nazli Goharian and Ophir Frieder},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IIT} {TREC} 2006: Genomics Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/iit.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/UrbainGF06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Combining Vector-Space and Word-Based Aspect Models for Passage Retrieval

_Raymond Wan, Ichigaku Takigawa, Hiroshi Mamitsuka, Vo Ngoc Anh_

- :fontawesome-solid-user-group: **Participant:** [kyotou.wan](./participants.md#kyotou.wan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/kyotou-umelbourne.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/kyotou-umelbourne.geo.final.pdf)
- :material-file-search: **Runs:** [kyoto2](./runs.md#kyoto2) | [kyoto20](./runs.md#kyoto20) | [kyoto1](./runs.md#kyoto1)

??? abstract "Abstract"
	
	This report summarizes the work done at Kyoto University and the University of Melbourne for the TREC 2006 Genomics Track. The single task for this year was to retrieve passages from a biomedical document collection. We devised a system made of two parts to deal with this problem. The first part was an existing IR system based on the vector-space model. The second part was a newly developed probabilistic word-based aspect model for identifying passages within relevant documents (or paragraphs).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/WanTMA06.bib) "
	```
	@inproceedings{DBLP:conf/trec/WanTMA06,
		author = {Raymond Wan and Ichigaku Takigawa and Hiroshi Mamitsuka and Vo Ngoc Anh},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Combining Vector-Space and Word-Based Aspect Models for Passage Retrieval},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/kyotou-umelbourne.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/WanTMA06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DUTIR at TREC 2006: Genomics and Enterprise Tracks

_Zhihao Yang, Hongfei Lin, Yanpeng Li, Linhong Xu, Yu Pan, Baoyan Liu_

- :fontawesome-solid-user-group: **Participant:** [dalianu.yang](./participants.md#dalianu.yang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/dalianu.geo.ent.final.pdf](http://trec.nist.gov/pubs/trec15/papers/dalianu.geo.ent.final.pdf)
- :material-file-search: **Runs:** [DUTgen1](./runs.md#dutgen1) | [DUTgen2](./runs.md#dutgen2) | [DUTgen3](./runs.md#dutgen3)

??? abstract "Abstract"
	
	This paper describes the techniques we applied for the two TREC 2006 tracks, i.e., Genomics and Enterprise track. For the Genomics Track, we used a Rocchio relevance feedback method to expand the terms and then performed passage retrieval by building dual index and using half overlapped windows passages. Several approaches to merge the results and rerank the passages are presented. For the Enterprise track, we stripped the non-letter character from documents and query, built the index by indri or lemur and established expert document pools.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangLLXPL06.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangLLXPL06,
		author = {Zhihao Yang and Hongfei Lin and Yanpeng Li and Linhong Xu and Yu Pan and Baoyan Liu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DUTIR} at {TREC} 2006: Genomics and Enterprise Tracks},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/dalianu.geo.ent.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangLLXPL06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### I2R at TREC 2006 Genomics Track

_Nie Yu, Lingpeng Yang, Jie Zhang, Jian Su, Dong-Hong Ji_

- :fontawesome-solid-user-group: **Participant:** [inst-infocomm-res.yu](./participants.md#inst-infocomm-res.yu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/iir.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/iir.geo.final.pdf)
- :material-file-search: **Runs:** [i2rg063](./runs.md#i2rg063) | [i2rg061](./runs.md#i2rg061) | [i2rg062](./runs.md#i2rg062)

??? abstract "Abstract"
	
	This paper describes the method we used for the Genomics Track of TREC 2006. BM25 model is implemented to retrieve relevant documents. We also tried to re-ranking documents based on the initial retrieval before passage retrieval. Passages are retrieved based on the concepts defining in topics and concept coverage. Results of submitted runs are listed and discussed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YuYJSJ06.bib) "
	```
	@inproceedings{DBLP:conf/trec/YuYJSJ06,
		author = {Nie Yu and Lingpeng Yang and Jie Zhang and Jian Su and Dong{-}Hong Ji},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{I2R} at {TREC} 2006 Genomics Track},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/iir.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YuYJSJ06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Using Profile Matching and Text Categorization for Answer Extraction  in TREC Genomics

_Haiqing Zheng, Chen Lin, Lishen Huang, Jun Xu, Jiaqian Zheng, Qi Sun, Junyu Niu_

- :fontawesome-solid-user-group: **Participant:** [fudanu.niu](./participants.md#fudanu.niu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/fudan-zheng.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/fudan-zheng.geo.final.pdf)
- :material-file-search: **Runs:** [fdugen1](./runs.md#fdugen1) | [fdugen3](./runs.md#fdugen3) | [fdugen2](./runs.md#fdugen2)

??? abstract "Abstract"
	
	TREC'06 genomics track was focusing on text mining and passage retrieval. WIM lab participated in this year's TREC genomics track. Our system consists of five parts: preprocessing, sentence generation, document retrieval, answer extraction and answer fusion. And we developed two different method: a automated profile matching-based method and a text categorization-based method to do the text mining, we will compare the performances between those two methods.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhengLHXZSN06.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhengLHXZSN06,
		author = {Haiqing Zheng and Chen Lin and Lishen Huang and Jun Xu and Jiaqian Zheng and Qi Sun and Junyu Niu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Using Profile Matching and Text Categorization for Answer Extraction in {TREC} Genomics},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/fudan-zheng.geo.final.pdf},
		timestamp = {Tue, 20 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhengLHXZSN06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Concept-Based Framework for Passage Retrieval at Genomics

_Wei Zhou, Clement T. Yu, Vetle I. Torvik, Neil R. Smalheiser_

- :fontawesome-solid-user-group: **Participant:** [uillinois.chicago.zhou](./participants.md#uillinois.chicago.zhou)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec15/papers/uillinois-chicago.geo.final.pdf](http://trec.nist.gov/pubs/trec15/papers/uillinois-chicago.geo.final.pdf)
- :material-file-search: **Runs:** [UICGenRun1](./runs.md#uicgenrun1) | [UICGenRun2](./runs.md#uicgenrun2) | [UICGenRun3](./runs.md#uicgenrun3)

??? abstract "Abstract"
	
	The task of TREC 2006 Genomics Track is to retrieve passages (from part to paragraph) from full-text HTML biomedical journal papers to answer the structured questions from real biologists. A system for such task needs to be able to parse the HTML free-texts (convert the HTML free-texts into plain texts) and pinpoint the most relevant passage(s) within documents for the specified question. This task is accomplished in three steps in our system. The first step is to parse the HTML articles and partition them into paragraphs. The second step is to retrieve the relevant paragraphs. The third step is to identify the most relevant passages within paragraphs and finally rank those passages. We are interested in 1. How does a concept-based IR model perform on structured queries comparing to Okapi? 2. Will the query expansion based on domain knowledge increase retrieval effectiveness? 3. Will our abbreviation database from MEDLINE help improve query expansion and will the abbreviation disambiguation help improve the ranking? The experiment results show that our concept-based IR model works better than the Okapi; query expansion based on domain knowledge is important, especially for those queries with very few relevant documents; an abbreviation database for query expansion and disambiguation is helpful for passage retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhouYTS06.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhouYTS06,
		author = {Wei Zhou and Clement T. Yu and Vetle I. Torvik and Neil R. Smalheiser},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Concept-Based Framework for Passage Retrieval at Genomics},
		booktitle = {Proceedings of the Fifteenth Text REtrieval Conference, {TREC} 2006, Gaithersburg, Maryland, USA, November 14-17, 2006},
		series = {{NIST} Special Publication},
		volume = {500-272},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2006},
		url = {http://trec.nist.gov/pubs/trec15/papers/uillinois-chicago.geo.final.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhouYTS06.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

