# Proceedings - Genomics 2005 

#### TREC 2005 Genomics Track Overview

_William R. Hersh, Aaron M. Cohen, Jianji Yang, Ravi Teja Bhupatiraju, Phoebe M. Roberts, Marti A. Hearst_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/GEO.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec14/papers/GEO.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The TREC 2005 Genomics Track featured two tasks, an ad hoc retrieval task and four subtasks in text categorization. The ad hoc retrieval task utilized a 10-year, 4.5-million document subset of the MEDLINE bibliographic database, with 50 topics conforming to five generic topic types. The categorization task used a full-text document collection with training and test sets consisting of about 6,000 biomedical journal articles each. Participants aimed to triage the documents into categories representing data resources in the Mouse Genome Informatics database, with performance assessed via a utility measure.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HershCYBRH05.bib) "
	```
	@inproceedings{DBLP:conf/trec/HershCYBRH05,
		author = {William R. Hersh and Aaron M. Cohen and Jianji Yang and Ravi Teja Bhupatiraju and Phoebe M. Roberts and Marti A. Hearst},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2005 Genomics Track Overview},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/GEO.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HershCYBRH05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Comparison of Techniques for Classification and Ad Hoc Retrieval  of Biomedical Documents

_Aaron M. Cohen, Jianji Yang, William R. Hersh_

- :fontawesome-solid-user-group: **Participant:** [ohsu.hersh](./participants.md#ohsu.hersh)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ohsu-geo.pdf](http://trec.nist.gov/pubs/trec14/papers/ohsu-geo.pdf)
- :material-file-search: **Runs:** [OHSUall](./runs.md#ohsuall) | [OHSUkey](./runs.md#ohsukey) | [AOHSUBF](./runs.md#aohsubf) | [AOHSUSL](./runs.md#aohsusl) | [AOHSUVP](./runs.md#aohsuvp) | [EOHSUBF](./runs.md#eohsubf) | [EOHSUSL](./runs.md#eohsusl) | [EOHSUVP](./runs.md#eohsuvp) | [GOHSUBF](./runs.md#gohsubf) | [GOHSUSL](./runs.md#gohsusl) | [GOHSUVP](./runs.md#gohsuvp) | [TOHSUBF](./runs.md#tohsubf) | [TOHSUSL](./runs.md#tohsusl) | [TOHSUVP](./runs.md#tohsuvp)

??? abstract "Abstract"
	
	Oregon Health & Science University participated in both the classification and ad hoc retrieval tasks of the TREC 2005 Genomics Track. To better understand the text classification techniques that lead to improved performance, we applied a set of general purpose biomedical document classification systems to the four triage tasks, varying one system feature or text processing technique at a time. We found that our best and most consistent system consisted of a voting perceptron classifier, chi-square feature selection on full text articles, binary feature weighting, stemming and stopping, and pre-filtering based on the MeSH term Mice. This system approached, but did not surpass, the performance of the best TREC entry for each of the four tasks. Full text provided a substantial benefit over only title plus abstract. Other common techniques such as inverse-document frequency feature weighting, and cosine normalization were ineffective. For the ad hoc retrieval task, we used Zettair search engine. Both of our submissions used Okapi measure with the parameters optimized using the sample topics that were provided. Two different query sets were used in our runs; one with all the words and the other with only the keywords from the topic file. Queries with only keywords consistently outperformed queries with all words from the topic file. Optimization of the Okapi parameters improved our performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CohenYH05.bib) "
	```
	@inproceedings{DBLP:conf/trec/CohenYH05,
		author = {Aaron M. Cohen and Jianji Yang and William R. Hersh},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Comparison of Techniques for Classification and Ad Hoc Retrieval of Biomedical Documents},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ohsu-geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CohenYH05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Retrieval of Biomedical Documents by Prioritizing Key Phrases

_Kevin Hsin-Yih Lin, Wen-Juan Hou, Hsin-Hsi Chen_

- :fontawesome-solid-user-group: **Participant:** [ntu.chen](./participants.md#ntu.chen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ntu.geo.adhoc.pdf](http://trec.nist.gov/pubs/trec14/papers/ntu.geo.adhoc.pdf)
- :material-file-search: **Runs:** [NTUgah1](./runs.md#ntugah1) | [NTUgah2](./runs.md#ntugah2) | [aNTUMAC](./runs.md#antumac) | [tNTUMAC](./runs.md#tntumac) | [eNTUMAC](./runs.md#entumac) | [gNTUMAC](./runs.md#gntumac) | [tNTUMACasem](./runs.md#tntumacasem) | [tNTUMACwj](./runs.md#tntumacwj)

??? abstract "Abstract"
	
	In this paper, we present an approach for retrieving relevant articles from the biomedical corpus. Our first run considered four kinds of operators as query expansion. The operators are phrase, mandatory, optional and synonym set. The second run lowered the ranking of documents which contained query terms only in their MeSH fields. The results of the official runs and further experiments were listed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinHC05.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinHC05,
		author = {Kevin Hsin{-}Yih Lin and Wen{-}Juan Hou and Hsin{-}Hsi Chen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Retrieval of Biomedical Documents by Prioritizing Key Phrases},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ntu.geo.adhoc.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LinHC05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Evaluation of Stemming, Query Expansion and Manual Indexing Approaches  for the Genomic Task

_Samir Abdou, Jacques Savoy, Patrick Ruch_

- :fontawesome-solid-user-group: **Participant:** [uneuchatel.savoy](./participants.md#uneuchatel.savoy)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uneuchatel.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/uneuchatel.geo.pdf)
- :material-file-search: **Runs:** [UniNeHug2c](./runs.md#uninehug2c) | [UniNeHug2](./runs.md#uninehug2)

??? abstract "Abstract"
	
	This paper describes our participation in TREC-2005 for the ad hoc Genomic track, in which we evaluate five different stemming approaches to performing domain-specific searches within a MEDLINE subset. We also evaluate the impact that manually assigned descriptors (MeSH headings) have on retrieval effectiveness. We design a domain-specific query expansion scheme and compare it with the more classic Rocchio approach. In our experiments on this collection subset, we discover that mean average precision does not improve when using different stemming algorithm. We then show how the presence of the MeSH headings significantly enhances mean average precision by about 9%. Finally, we illustrate how the use of various query expansion techniques can impairs retrieval performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AbdouSR05.bib) "
	```
	@inproceedings{DBLP:conf/trec/AbdouSR05,
		author = {Samir Abdou and Jacques Savoy and Patrick Ruch},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Evaluation of Stemming, Query Expansion and Manual Indexing Approaches for the Genomic Task},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uneuchatel.geo.pdf},
		timestamp = {Wed, 07 Jul 2021 16:44:22 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AbdouSR05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2005 Genomics Track Experiments at IBM Watson

_Rie Kubota Ando, Mark Dredze, Tong Zhang_

- :fontawesome-solid-user-group: **Participant:** [ibm.zhang](./participants.md#ibm.zhang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ibm-tjwatson.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/ibm-tjwatson.geo.pdf)
- :material-file-search: **Runs:** [ibmadz05bs](./runs.md#ibmadz05bs) | [ibmadz05us](./runs.md#ibmadz05us) | [aibmadz05m1](./runs.md#aibmadz05m1) | [eibmadz05m1](./runs.md#eibmadz05m1) | [gibmadz05m1](./runs.md#gibmadz05m1) | [tibmadz05m1](./runs.md#tibmadz05m1) | [aibmadz05m2](./runs.md#aibmadz05m2) | [eibmadz05m2](./runs.md#eibmadz05m2) | [gibmadz05m2](./runs.md#gibmadz05m2) | [tibmadz05m2](./runs.md#tibmadz05m2) | [aibmadz05s](./runs.md#aibmadz05s) | [eibmadz05s](./runs.md#eibmadz05s) | [gibmadz05s](./runs.md#gibmadz05s) | [tibmadz05s](./runs.md#tibmadz05s)

??? abstract "Abstract"
	
	This paper describes our experiments in the TREC 2005 Genomics Track. For the ad-hoc retrieval task, we study synonym-based query expan-sion, as well as the effectiveness of a new pseudo-relevance feedback method which is derived from our recent work on semi-supervised learning. For the categorization task, we study various methods for estimating conditional class probability and determining the optimal threshold parameter - essential for obtaining high performance results for this task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AndoDZ05.bib) "
	```
	@inproceedings{DBLP:conf/trec/AndoDZ05,
		author = {Rie Kubota Ando and Mark Dredze and Tong Zhang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2005 Genomics Track Experiments at {IBM} Watson},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ibm-tjwatson.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AndoDZ05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Fusion of Knowledge-Intensive and Statistical Approaches for Retrieving  and Annotating Textual Genomics Documents

_Alan R. Aronson, Dina Demner-Fushman, Susanne M. Humphrey, Jimmy Lin, Patrick Ruch, Miguel E. Ruiz, Lawrence H. Smith, Lorraine K. Tanabe, W. John Wilbur, Hongfang Liu_

- :fontawesome-solid-user-group: **Participant:** [nlm-umd.aronson](./participants.md#nlm-umd.aronson)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/nlm-umd.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/nlm-umd.geo.pdf)
- :material-file-search: **Runs:** [NLMfusionA](./runs.md#nlmfusiona) | [NLMfusionB](./runs.md#nlmfusionb) | [aNLMF](./runs.md#anlmf) | [eNLMF](./runs.md#enlmf) | [gNLMF](./runs.md#gnlmf) | [tNLMF](./runs.md#tnlmf) | [NLM2A](./runs.md#nlm2a) | [NLM2E](./runs.md#nlm2e) | [NLM2G](./runs.md#nlm2g) | [NLM2T](./runs.md#nlm2t) | [aNLMB](./runs.md#anlmb) | [NLM1T](./runs.md#nlm1t) | [eNLMKNN](./runs.md#enlmknn) | [NLM1G](./runs.md#nlm1g)

??? abstract "Abstract"
	
	This paper represents a continuation of research into the retrieval and annotation of textual genomics documents (both MEDLINE® citations and full text articles) for the purpose of satisfying biologists' real information needs. The overall approach taken here for both the ad hoc retrieval and categorization tasks within the TREC genomics track in 2005 was one combining the results of several NLP, statistical and ML methods, using a fusion method for ad hoc retrieval and ensemble methods for categorization. The results show that fusion approaches can improve the final outcome for the ad hoc and the categorization tasks, but that care must be taken in order to take advantage of the strengths of the constituent methods.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AronsonDHLRRSTWL05.bib) "
	```
	@inproceedings{DBLP:conf/trec/AronsonDHLRRSTWL05,
		author = {Alan R. Aronson and Dina Demner{-}Fushman and Susanne M. Humphrey and Jimmy Lin and Patrick Ruch and Miguel E. Ruiz and Lawrence H. Smith and Lorraine K. Tanabe and W. John Wilbur and Hongfang Liu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Fusion of Knowledge-Intensive and Statistical Approaches for Retrieving and Annotating Textual Genomics Documents},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/nlm-umd.geo.pdf},
		timestamp = {Fri, 27 Aug 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/AronsonDHLRRSTWL05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Classifying Biomedical Articles by Making Localized Decisions

_Thomas Brow, Burr Settles, Mark Craven_

- :fontawesome-solid-user-group: **Participant:** [uwisconsin.craven](./participants.md#uwisconsin.craven)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uwisconsin.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/uwisconsin.geo.pdf)
- :material-file-search: **Runs:** [Afull](./runs.md#afull) | [Efull](./runs.md#efull) | [Gfull](./runs.md#gfull) | [Tfull](./runs.md#tfull) | [Apars](./runs.md#apars) | [Epars](./runs.md#epars) | [Gpars](./runs.md#gpars) | [Tpars](./runs.md#tpars) | [Ameta](./runs.md#ameta) | [Emeta](./runs.md#emeta) | [Gmeta](./runs.md#gmeta) | [Tmeta](./runs.md#tmeta)

??? abstract "Abstract"
	
	We describe a system developed for the Categorization task of the Text Retrieval Conference (TREC) 2005 Genomics track, and experiments we conducted in the process of developing our system. Our research effort for this task explored the hypothesis that more accurate predictions could be achieved by considering only selected passages in the documents being processed. We investigated methods that involve (i) basing classifications on selected passages from test articles, and (ii) adjusting the classifier training process such that certain putatively relevant passages affect the learned model more than other passages. Whereas the first approach was effective at improving predictive accuracy in our experiments, the latter approach was not
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BrowSC05.bib) "
	```
	@inproceedings{DBLP:conf/trec/BrowSC05,
		author = {Thomas Brow and Burr Settles and Mark Craven},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Classifying Biomedical Articles by Making Localized Decisions},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uwisconsin.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BrowSC05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Structural Term Extraction for Expansion of Template-Based Genomic  Queries

_Fabrice Camous, Stephen Blott, Cathal Gurrin, Gareth J. F. Jones, Alan F. Smeaton_

- :fontawesome-solid-user-group: **Participant:** [dublincityu.gurrin](./participants.md#dublincityu.gurrin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/dublincu.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/dublincu.geo.pdf)
- :material-file-search: **Runs:** [dcu1](./runs.md#dcu1) | [dcu2](./runs.md#dcu2)

??? abstract "Abstract"
	
	This paper describes our experiments run to address the ad hoc task of the TREC 2005 Genomics track. The task topics were expressed with 5 different structures called Generic Topic Templates (GTTs). We hypothesized the presence of GTT-specific structural terms in the free-text fields of documents relevant to a topic instantiated from that same GTT. Our experiments aimed at extracting and selecting candidate structural terms for each GTT. Selected terms were used to expand initial queries and the quality of the term selection was measured by the impact of the expansion on initial search results. The evaluation used the task training topics and the associated relevance information. This paper describes the two term extraction methods used in the experiments and the resulting two runs sent to NIST for evaluation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CamousBGJS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/CamousBGJS05,
		author = {Fabrice Camous and Stephen Blott and Cathal Gurrin and Gareth J. F. Jones and Alan F. Smeaton},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Structural Term Extraction for Expansion of Template-Based Genomic Queries},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/dublincu.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CamousBGJS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Concept Recognition and the TREC Genomics Tasks

_J. Gregory Caporaso, William A. Baumgartner Jr., K. Bretonnel Cohen, Helen L. Johnson, Jesse Paquette, Lawrence Hunter_

- :fontawesome-solid-user-group: **Participant:** [ucolorado.cohen](./participants.md#ucolorado.cohen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ucolorado-hsc.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/ucolorado-hsc.geo.pdf)
- :material-file-search: **Runs:** [CCP0](./runs.md#ccp0) | [CCP1](./runs.md#ccp1) | [aUCHSCnb1En3](./runs.md#auchscnb1en3) | [eUCHSCnb1En3](./runs.md#euchscnb1en3) | [gUCHSCnb1En3](./runs.md#guchscnb1en3) | [tUCHSCnb1En3](./runs.md#tuchscnb1en3) | [aUCHSCnb1En4](./runs.md#auchscnb1en4) | [eUCHSCnb1En4](./runs.md#euchscnb1en4) | [gUCHSCnb1En4](./runs.md#guchscnb1en4) | [tUCHSCnb1En4](./runs.md#tuchscnb1en4) | [aUCHSCsvm](./runs.md#auchscsvm) | [eUCHSCsvm](./runs.md#euchscsvm) | [gUCHSCsvm](./runs.md#guchscsvm) | [tUCHSCsvm](./runs.md#tuchscsvm)

??? abstract "Abstract"
	
	We applied concept recognition techniques to the Genomics track primary and secondary tasks. For the primary task, we developed a foundational information retrieval system which incorporated Entrez Gene entries and UMLS concepts for query expansion via phrasal and term boosting representations of synonyms. For the secondary task, we evaluated three conceptual features—mouse strain names, indexed MeSH terms, and normalized citations—in addition to two surface linguistic features—BOW and bigrams. Our final feature set yielded consistently high F-measures.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CaporasoBCJPH05.bib) "
	```
	@inproceedings{DBLP:conf/trec/CaporasoBCJPH05,
		author = {J. Gregory Caporaso and William A. Baumgartner Jr. and K. Bretonnel Cohen and Helen L. Johnson and Jesse Paquette and Lawrence Hunter},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Concept Recognition and the {TREC} Genomics Tasks},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ucolorado-hsc.geo.pdf},
		timestamp = {Tue, 26 Jan 2021 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CaporasoBCJPH05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DIMACS at the TREC 2005 Genomics Track

_Aynur A. Dayanik, Alexander Genkin, Paul B. Kantor, David D. Lewis, David Madigan_

- :fontawesome-solid-user-group: **Participant:** [rutgers.dayanik](./participants.md#rutgers.dayanik)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/rutgersu-dimacs.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/rutgersu-dimacs.geo.pdf)
- :material-file-search: **Runs:** [aDIMACSg9md](./runs.md#adimacsg9md) | [eDIMACSg9md](./runs.md#edimacsg9md) | [gDIMACSg9md](./runs.md#gdimacsg9md) | [tDIMACSg9md](./runs.md#tdimacsg9md) | [aDIMACSg9w](./runs.md#adimacsg9w) | [eDIMACSg9w](./runs.md#edimacsg9w) | [gDIMACSg9w](./runs.md#gdimacsg9w) | [tDIMACSg9w](./runs.md#tdimacsg9w) | [aDIMACSl9w](./runs.md#adimacsl9w) | [eDIMACSl9w](./runs.md#edimacsl9w) | [gDIMACSl9w](./runs.md#gdimacsl9w) | [tDIMACSl9w](./runs.md#tdimacsl9w) | [aDIMACSl9md](./runs.md#adimacsl9md) | [eDIMACSl9md](./runs.md#edimacsl9md) | [gDIMACSl9md](./runs.md#gdimacsl9md) | [tDIMACSl9md](./runs.md#tdimacsl9md)

??? abstract "Abstract"
	
	This report describes DIMACS work on the text categorization task of the TREC 2005 Genomics track. Our approach to this task was similar to the triage subtask studied in the TREC 2004 Genomics track. We applied Bayesian logistic regression and achieved good effectiveness on all categories.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DayanikGKLM05.bib) "
	```
	@inproceedings{DBLP:conf/trec/DayanikGKLM05,
		author = {Aynur A. Dayanik and Alexander Genkin and Paul B. Kantor and David D. Lewis and David Madigan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DIMACS} at the {TREC} 2005 Genomics Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/rutgersu-dimacs.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DayanikGKLM05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments in Questions and Relationships at the University of Iowa

_David Eichmann, Padmini Srinivasan_

- :fontawesome-solid-user-group: **Participant:** [uiowa.eichmann](./participants.md#uiowa.eichmann)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uiowa.geo.qa.pdf](http://trec.nist.gov/pubs/trec14/papers/uiowa.geo.qa.pdf)
- :material-file-search: **Runs:** [UIowa05GN101](./runs.md#uiowa05gn101) | [UIowa05GN102](./runs.md#uiowa05gn102)

??? abstract "Abstract"
	
	The University of Iowa participated in the genomics and question answering tracks of TREC-2005. This paper covers only our work in question answering.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EichmannS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/EichmannS05,
		author = {David Eichmann and Padmini Srinivasan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments in Questions and Relationships at the University of Iowa},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uiowa.geo.qa.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EichmannS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### CSUSM at TREC 2005: Genomics and Enterprise Track

_Rocio Guillén_

- :fontawesome-solid-user-group: **Participant:** [csusm.guillen](./participants.md#csusm.guillen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/calstateu-sanmarcos.geo.ent.pdf](http://trec.nist.gov/pubs/trec14/papers/calstateu-sanmarcos.geo.ent.pdf)
- :material-file-search: **Runs:** [genome1](./runs.md#genome1) | [genome2](./runs.md#genome2) | [Tcsusm1](./runs.md#tcsusm1) | [Tcsusm2](./runs.md#tcsusm2)

??? abstract "Abstract"
	
	In this paper we report on the approach, experiments and results for the Enterprise Track and the Genomics Track. We participated in the adhoc and one of the categorization tasks for the Genomics track. For the enterprise track we participated in the known-item search. We ran experiments using Indri (1], which combines inference networks with language modeling, for the adhoc and the known-item search tasks. For the categorization task we filtered the documents in different stages using decision trees.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Guillen05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Guillen05,
		author = {Rocio Guill{\'{e}}n},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{CSUSM} at {TREC} 2005: Genomics and Enterprise Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/calstateu-sanmarcos.geo.ent.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Guillen05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UM-D at TREC 2005: Genomics Track

_Liping Huang, ZhiHang Chen, Yi Lu Murphey_

- :fontawesome-solid-user-group: **Participant:** [umichigan-dearborn.murphey](./participants.md#umichigan-dearborn.murphey)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/umich-dearborn.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/umich-dearborn.geo.pdf)
- :material-file-search: **Runs:** [UMD01](./runs.md#umd01) | [UMD02](./runs.md#umd02)

??? abstract "Abstract"
	
	The University of Michigan-Dearborn team participated in the ad hoc task and submitted two runs in TREC 2005. The Genomics track is different from others since it focuses on document retrieval in genomics domain as opposed to general retrieval tasks such as question-answering, multi-lingual IR, etc. Since we were not familiar with the knowledge in biomedical field, we utilized the database publicly available online to obtain alias and variations of names for genes/proteins. We generated a term list based on each topic description and their alias and variations. The terms were further transformed into a logical expression in which terms were connected by “AND” and “OR”. The documents satisfying the logical expression are retrieved and their similarity scores are calculated based on the weighted terms using the method of Okapi BM25 proposed by Robertson et al[RWJ94][RWB98] [BCC04].
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HuangCM05.bib) "
	```
	@inproceedings{DBLP:conf/trec/HuangCM05,
		author = {Liping Huang and ZhiHang Chen and Yi Lu Murphey},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UM-D} at {TREC} 2005: Genomics Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/umich-dearborn.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HuangCM05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2005: Genomics Track

_Xiangji Huang, Ming Zhong, Luo Si_

- :fontawesome-solid-user-group: **Participant:** [yorku.huang](./participants.md#yorku.huang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/yorku-huang2.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/yorku-huang2.geo.pdf)
- :material-file-search: **Runs:** [york05ga1](./runs.md#york05ga1) | [york05gm1](./runs.md#york05gm1) | [york05ga2](./runs.md#york05ga2) | [york05ga3](./runs.md#york05ga3) | [york05ga4](./runs.md#york05ga4) | [york05ga5](./runs.md#york05ga5)

??? abstract "Abstract"
	
	Our Genomics experiments mainly focus on addressing three major problems in biomedical information retrieval. The three problems are: (1) how to deal with synonyms? (2) how to deal with the frequent use of acronyms? (3) how to deal with homonyms? In particular, we propose two query expansion algorithms to construct structured queries for our experiments. The mean average precision (MAP) for our automatic run “york05ga1” using Algorithm 1 was 0.2888 and for our manual run “york05gm1” using Algorithm 2 was 0.3020. The evaluation results show that both algorithms are effective for improving retrieval performance. We also find that some other techniques such as pseudo-relevance feedback and using an extended stop word set can make positive contributions to the retrieval performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HuangZS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/HuangZS05,
		author = {Xiangji Huang and Ming Zhong and Luo Si},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {York University at {TREC} 2005: Genomics Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/yorku-huang2.geo.pdf},
		timestamp = {Tue, 05 Sep 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HuangZS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Pattern Based Customized Learning for TREC Genomics Track Categorization  Task

_Wai Lam, Yiqiu Han, Ki Chan_

- :fontawesome-solid-user-group: **Participant:** [cuhk.lam](./participants.md#cuhk.lam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/chineseu-hongkong-lam.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/chineseu-hongkong-lam.geo.pdf)
- :material-file-search: **Runs:** [cuhkrun1](./runs.md#cuhkrun1) | [cuhkrun1E](./runs.md#cuhkrun1e) | [cuhkrun1G](./runs.md#cuhkrun1g) | [cuhkrun1T](./runs.md#cuhkrun1t) | [cuhkrun2A](./runs.md#cuhkrun2a) | [cuhkrun2E](./runs.md#cuhkrun2e) | [cuhkrun2G](./runs.md#cuhkrun2g) | [cuhkrun2T](./runs.md#cuhkrun2t) | [cuhkrun3A](./runs.md#cuhkrun3a) | [cuhkrun3G](./runs.md#cuhkrun3g) | [cuhkrun3T](./runs.md#cuhkrun3t) | [cuhkrun3E](./runs.md#cuhkrun3e)

??? abstract "Abstract"
	
	Our group participated in the categorization task in the TREC Genomics Track  2005, where biological literatures have to be categorized into four types of information. Our approach to this problem adopts customized learning methods in model learning  and document categorization. Our pattern-based learning approach can discover useful patterns for tackling categorization challenges.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LamHC05.bib) "
	```
	@inproceedings{DBLP:conf/trec/LamHC05,
		author = {Wai Lam and Yiqiu Han and Ki Chan},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Pattern Based Customized Learning for {TREC} Genomics Track Categorization Task},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/chineseu-hongkong-lam.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LamHC05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Identifying Relevant Full-Text Articles for Database Curation

_Chih Lee, Wen-Juan Hou, Hsin-Hsi Chen_

- :fontawesome-solid-user-group: **Participant:** [ntu.chen](./participants.md#ntu.chen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ntu.geo.cate.pdf](http://trec.nist.gov/pubs/trec14/papers/ntu.geo.cate.pdf)
- :material-file-search: **Runs:** [NTUgah1](./runs.md#ntugah1) | [NTUgah2](./runs.md#ntugah2) | [aNTUMAC](./runs.md#antumac) | [tNTUMAC](./runs.md#tntumac) | [eNTUMAC](./runs.md#entumac) | [gNTUMAC](./runs.md#gntumac) | [tNTUMACasem](./runs.md#tntumacasem) | [tNTUMACwj](./runs.md#tntumacwj)

??? abstract "Abstract"
	
	In this paper, we propose an approach for identifying curatable articles from a large pool. Our system currently considers three parts of an article as three individual representations of the article, and utilizes two domain-specific resources to reveal the deep knowledge contained in the article in order to generate more representations of the article. Cross-validation is employed to find the best combination of representations and an SVM classifier is trained out of this combination. The cross-validation results and results of the official runs are listed. The experimental results show overall high performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LeeHC05.bib) "
	```
	@inproceedings{DBLP:conf/trec/LeeHC05,
		author = {Chih Lee and Wen{-}Juan Hou and Hsin{-}Hsi Chen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Identifying Relevant Full-Text Articles for Database Curation},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ntu.geo.cate.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LeeHC05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Learning Domain-Specific Knowledge from Context–THUIR at TREC 2005  Genomics Track

_Jiao Li, Xian Zhang, Yu Hao, Minlie Huang, Xiaoyan Zhu_

- :fontawesome-solid-user-group: **Participant:** [tsinghua.ma](./participants.md#tsinghua.ma)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/tsinghuau-ma.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/tsinghuau-ma.geo.pdf)
- :material-file-search: **Runs:** [THUIRgen1S](./runs.md#thuirgen1s) | [THUIRgen2P](./runs.md#thuirgen2p) | [THUIRgenA1p1](./runs.md#thuirgena1p1) | [THUIRgenE1p8](./runs.md#thuirgene1p8) | [THUIRgenG1p1](./runs.md#thuirgeng1p1) | [THUIRgenT1p5](./runs.md#thuirgent1p5) | [THUIRgenGMNG](./runs.md#thuirgengmng) | [THUIRgA0p9x](./runs.md#thuirga0p9x)

??? abstract "Abstract"
	
	We(Tsinghua University) participated both Ad Hoc Retrieval Task and Categorization Task in TREC2005 Genomics Track, in which we designed and implemented a serious of methods encompassed learning domain-specific knowledge from context. In Ad Hoc Retrieval Task, internal resource is introduced to expand query, different granularity indexing provides more flexible retrieval space, and pattern discovering imports Information Extraction (IE) concept into Information Retrieval (IR). In Categorization Task, instead of the single word feature, we presented Seed-based Loose N-gram Feature, which achieved success in the four subtasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiZHHZ05.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiZHHZ05,
		author = {Jiao Li and Xian Zhang and Yu Hao and Minlie Huang and Xiaoyan Zhu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Learning Domain-Specific Knowledge from Context--THUIR at {TREC} 2005 Genomics Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/tsinghuau-ma.geo.pdf},
		timestamp = {Thu, 02 Feb 2023 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiZHHZ05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### A Menagerie of Tracks at Maryland: HARD, Enterprise, QA, and Genomics,  Oh My!

_Jimmy Lin, Eileen G. Abels, Dina Demner-Fushman, Douglas W. Oard, Philip Fei Wu, Yejun Wu_

- :fontawesome-solid-user-group: **Participant:** [umaryland.oard](./participants.md#umaryland.oard)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/umaryland-lin.hard.ent.qa.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/umaryland-lin.hard.ent.qa.geo.pdf)
- :material-file-search: **Runs:** [MARYGEN1](./runs.md#marygen1)

??? abstract "Abstract"
	
	This year, the University of Maryland participated in four separate tracks: HARD, enterprise, question answering, and genomics. Our HARD experiments involved a trained intermediary who searched for documents on behalf of the user, created clarification forms manually, and exploited user responses accordingly. The aim was to better understand the nature of single-iteration clarification dialogs and to develop an “ontology of clarifications” that can be leveraged to guide system development. For the enterprise track, we submitted official runs to the Known Item Search and the Discussion Search tasks. Document transformation to normalize dates and version numbers was found to be helpful, but suppression of text quoted from earlier messages and expansion of the indexed terms for a message based on subject line threading proved to not be. For the QA track, we submitted a manual run of “other” questions in an effort to quantify human performance on the task. Our genomics track participation was in collaboration with the National Library of Medicine, and is primarily reported in NLM's overview paper.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LinADOWW05.bib) "
	```
	@inproceedings{DBLP:conf/trec/LinADOWW05,
		author = {Jimmy Lin and Eileen G. Abels and Dina Demner{-}Fushman and Douglas W. Oard and Philip Fei Wu and Yejun Wu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {A Menagerie of Tracks at Maryland: HARD, Enterprise, QA, and Genomics, Oh My!},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/umaryland-lin.hard.ent.qa.geo.pdf},
		timestamp = {Sat, 29 Jul 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/LinADOWW05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Combining Thesauri-Based Methods for Biomedical Retrieval

_Edgar Meij, Leonie IJzereef, Leif Azzopardi, Jaap Kamps, Maarten de Rijke_

- :fontawesome-solid-user-group: **Participant:** [uamsterdam.aidteam](./participants.md#uamsterdam.aidteam)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uamsterdam-infoinst.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/uamsterdam-infoinst.geo.pdf)
- :material-file-search: **Runs:** [UAmscombGeFb](./runs.md#uamscombgefb) | [UAmscombGeMl](./runs.md#uamscombgeml)

??? abstract "Abstract"
	
	This paper describes our participation in the TREC 2005 Genomics track. We took part in the ad hoc retrieval task and aimed at integrating thesauri in the retrieval model. We developed three thesauri-based methods, two of which made use of the existing MeSH thesaurus. One method uses blind relevance feedback on MeSH terms, the second uses an index of the MeSH thesaurus for query expansion. The third method makes use of a dynamically generated lookup list, by which acronyms and synonyms could be inferred. We show that, despite the relatively minor improvements in retrieval performance of individually applied methods, a combination works best and is able to deliver significant improvements over the baseline.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/MeijIAKR05.bib) "
	```
	@inproceedings{DBLP:conf/trec/MeijIAKR05,
		author = {Edgar Meij and Leonie IJzereef and Leif Azzopardi and Jaap Kamps and Maarten de Rijke},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Combining Thesauri-Based Methods for Biomedical Retrieval},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uamsterdam-infoinst.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/MeijIAKR05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WIM at TREC 2005

_Junyu Niu, Lin Sun, Luqun Lou, Fang Deng, Chen Lin, Haiqing Zheng, Xuanjing Huang_

- :fontawesome-solid-user-group: **Participant:** [fudan.niu](./participants.md#fudan.niu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/fudanu-sun.geo.ent.pdf](http://trec.nist.gov/pubs/trec14/papers/fudanu-sun.geo.ent.pdf)
- :material-file-search: **Runs:** [wim1](./runs.md#wim1) | [wim2](./runs.md#wim2) | [aFduMarsI](./runs.md#afdumarsi) | [eFduMarsI](./runs.md#efdumarsi) | [gFduMarsI](./runs.md#gfdumarsi) | [tFduMarsI](./runs.md#tfdumarsi) | [aFduMarsII](./runs.md#afdumarsii) | [eFduMarsII](./runs.md#efdumarsii) | [gFduMarsII](./runs.md#gfdumarsii) | [tFduMarsII](./runs.md#tfdumarsii) | [aFduMarsIII](./runs.md#afdumarsiii) | [eFduMarsIII](./runs.md#efdumarsiii) | [gFduMarsIII](./runs.md#gfdumarsiii) | [tFduMarsIII](./runs.md#tfdumarsiii)

??? abstract "Abstract"
	
	This paper describes the three TREC tasks we participated in this year, which are, Genomics track's categorization task and ad hoc task, and Enterprise track's known item search task. For the categorization task, we adopt a domain-specific terms extraction method and an ontology-based method for feature selection. A SVM classifier and a Rocchio based two staged classifier were also used in this experiment. For the ad-hoc task, we used BM25 algorithm, probabilistic model and query expansion. For the Enterprise track, language model was adopted, and entity recognition was also implemented in our experiment.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NiuSLDLZH05.bib) "
	```
	@inproceedings{DBLP:conf/trec/NiuSLDLZH05,
		author = {Junyu Niu and Lin Sun and Luqun Lou and Fang Deng and Chen Lin and Haiqing Zheng and Xuanjing Huang},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WIM} at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/fudanu-sun.geo.ent.pdf},
		timestamp = {Tue, 20 Jul 2021 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/NiuSLDLZH05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2005 Genomics Track Experiments at UTA

_Ari Pirkola_

- :fontawesome-solid-user-group: **Participant:** [utampere.pirkola](./participants.md#utampere.pirkola)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/utampere.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/utampere.geo.pdf)
- :material-file-search: **Runs:** [uta05a](./runs.md#uta05a) | [uta05i](./runs.md#uta05i)

??? abstract "Abstract"
	
	University of Tampere submitted runs for Genomics Track ad hoc retrieval task. The first run (uta05a) was an automatic and the second (uta05i) an interactive run. The uta05a queries were constructed by using the original topic terms as query keys. The uta05a queries served as a baseline for the uta05i queries which were constructed by expanding the uta05a queries with synonyms for the topic gene names from the Entrez Gene database and by further expanding with synonymous gene names and MH terms from the top documents of an initial uta05i search. The mean average precision for uta05a was 0.2385 and for uta05i 0.1980. Next in Section 2.1 we present the indexing methods and the processing of query keys. Section 2.2 considers the retrieval system and query operators. Query formulation is presented in Section 2.3. Section 3 contains the results and conclusions.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Pirkola05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Pirkola05,
		author = {Ari Pirkola},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2005 Genomics Track Experiments at {UTA}},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/utampere.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Pirkola05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Report on the TREC 2005 Experiment: Genomics Track

_Patrick Ruch, Frédéric Ehrler, Samir Abdou, Jacques Savoy_

- :fontawesome-solid-user-group: **Participant:** [u.geneva](./participants.md#u.geneva)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uhospital-geneva.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/uhospital-geneva.geo.pdf)
- :material-file-search: **Runs:** [UniGeNe](./runs.md#unigene) | [UniGe2](./runs.md#unige2)

??? abstract "Abstract"
	
	This year, for our participation to the TREC Genomics track, we participated in the two tasks: the ad hoc and the categorization task. In this notebook report, we do not detail our experiments, which will be described more precisely in the final proceedings. This papers focuses on the ad hoc task, while experiments conducted for task 2 are described in the Aronson and al. 2005. Task I. For the ad hoc retrieval task, we used the easyIR tool, a standard vector-space engine developed at the University of Geneva. Our approach uses thesaural resources together with a variant of the Porter stemmer for string normalization. Gene and Protein Entities (GPE) in queries are marked up by dictionary look up at retrieval time in order to be expanded using a gene and protein thesaurus. For indexing the Genomic collection, the following MEDLINE records were selected: article's titles, MeSH and RN terms, and abstract fields. Following observations made on MEDLINE documents regarding their length distribution, we decided to rely on a slightly modified dtu.dtn weighting schema. This constitutes our baseline run (Baseline=0.2312; Baseline+expansion=0.2373). Finally, we used a run provided by the University of Neuchâtel, which features thesaurus-based GPE expansion and automatic feed back (UniGeNe=0.2150) to produce a third run, which achieved our best results (UniGe2=0.2396).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RuchEAS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/RuchEAS05,
		author = {Patrick Ruch and Fr{\'{e}}d{\'{e}}ric Ehrler and Samir Abdou and Jacques Savoy},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Report on the {TREC} 2005 Experiment: Genomics Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uhospital-geneva.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RuchEAS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments on Genomics Ad Hoc Retrieval

_Miguel E. Ruiz_

- :fontawesome-solid-user-group: **Participant:** [suny-buffalo.ruiz](./participants.md#suny-buffalo.ruiz)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/stateu-ny-buffalo.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/stateu-ny-buffalo.geo.pdf)
- :material-file-search: **Runs:** [UBIgeneA](./runs.md#ubigenea)

??? abstract "Abstract"
	
	This paper represents te results of the State University of New York at Buffalo (School of Informatics) in the TREC 2005 Conference. We participated in the Genomics ad hoc retrieval task. Our approach used the SMART system for indexing the large collection of MEDLINE documents. For this purpose we used a distributed retrieval approach and divided the large collection into 5 non overlapping sub collections. We tried several approaches on the training topics to select the best run possible. Our results perform slightly above the median system in the conference. We also paired with the NLM team to contribute a run for their fusion approach.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Ruiz05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Ruiz05,
		author = {Miguel E. Ruiz},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments on Genomics Ad Hoc Retrieval},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/stateu-ny-buffalo.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Ruiz05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2005 Genomics Track A Concept-Based Approach to Text Categorization

_Bob J. A. Schijvenaars, Martijn J. Schuemie, Erik M. van Mulligen, Marc Weeber, Rob Jelier, Barend Mons, Jan A. Kors, Wessel Kraaij_

- :fontawesome-solid-user-group: **Participant:** [erasmus.kors](./participants.md#erasmus.kors)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/erasmus-tno.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/erasmus-tno.geo.pdf)
- :material-file-search: **Runs:** [ABPLUS](./runs.md#abplus) | [ABPLUSE](./runs.md#abpluse) | [ABPLUSG](./runs.md#abplusg) | [ABPLUST](./runs.md#abplust) | [FTA](./runs.md#fta) | [FTE](./runs.md#fte) | [FTT](./runs.md#ftt) | [FTG](./runs.md#ftg)

??? abstract "Abstract"
	
	The Biosemantics group (Erasmus University Medical Center, Rotterdam) participated in the text categorization task of the Genomics Track. We followed a thesaurus-based approach, using the Collexis indexing system, in combination with a simple classification algorithm to assign a document to one of the four categories. Our thesaurus consisted of a combination of MeSH, Gene Ontology, and a thesaurus with gene and protein symbols and names extracted from the Mouse Genome Database, Swiss-Prot and Entrez Gene. To increase the coverage of the gene thesaurus, several rewrite rules were applied to take possible spelling variations into account. Each document in the training set was indexed and the found concepts were ranked on term frequency, resulting in one concept vector per document. No particular care was taken to resolve ambiguous terms. For each of the four categories, two average concept vectors were computed, one by averaging the concept vectors of the documents in that category and the other by averaging all remaining concept vectors. The latter vector was then subtracted from the first, yielding a final category concept vector. The subtraction served to emphasize distinguishing concepts: high-ranked concepts in the final concept vector should, on average, occur relatively frequently in documents belonging to the category, while occurring infrequently or not at all in documents not belonging to the category. For all documents in the training set, a matching score between the concept vector of a document and each of the category concept vectors was computed. A score threshold to discriminate between category and non-category documents was then determined per category by optimizing the performance measure (normalized utility). Different matching algorithms and different cutoffs for the number of concepts in the category vectors were evaluated. A standard cosine similarity score and a category vector with the 40 highest-ranking concepts proved to perform best on the training set. These settings and the score thresholds were subsequently used to categorize all documents in the test set. Two runs were submitted: one based on the full text without any special treatment of particular sections, and one based on the Medline abstract, including the title and the MeSH headings. In addition two runs were submitted by TNO for the ad-hoc search task. The ad-hoc system was based on the TREC 2004 system, with a small experiment trying to leverage information about the authority level of specific journals.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SchijvenaarsSMWJMKK05.bib) "
	```
	@inproceedings{DBLP:conf/trec/SchijvenaarsSMWJMKK05,
		author = {Bob J. A. Schijvenaars and Martijn J. Schuemie and Erik M. van Mulligen and Marc Weeber and Rob Jelier and Barend Mons and Jan A. Kors and Wessel Kraaij},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2005 Genomics Track {A} Concept-Based Approach to Text Categorization},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/erasmus-tno.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SchijvenaarsSMWJMKK05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Synonym-Based Expansion and Boosting-Based Re-Ranking: A Two-phase  Approach for Genomic Information Retrieval

_Zhongmin Shi, Baohua Gu, Fred Popowich, Anoop Sarkar_

- :fontawesome-solid-user-group: **Participant:** [simon-fraseru.shi](./participants.md#simon-fraseru.shi)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/simon-fraseru.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/simon-fraseru.geo.pdf)
- :material-file-search: **Runs:** [SFUshi](./runs.md#sfushi)

??? abstract "Abstract"
	
	We describe in this paper the design and evaluation of the system built at Simon Fraser University for the TREC 2005 adhoc retrieval task in the Genomics track. The main approach taken in our system was to expand synonyms by exploiting a fusion of a set of biomedical and general ontology sources, and apply machine learning and natural language processing techniques to re-rank retrieved documents. In our system, we integrated EntrezGene, HUGO, Eugenes, ARGH, GO, MeSH, UMLSKS and WordNet into a large reference database and then used a conventional Information Retrieval (IR) toolkit, the Lemur toolkit (Lemur, 2005), to build an IR system. In the post-processing phase, we applied a boosting algorithm (Kudo and Matsumoto, 2004) that captured natural language substructures embedded in texts to re-rank the retrieved documents. Experimental results show that the boosting algorithm worked well in cases where a conventional IR system performs poorly, but this re-ranking approach was not robust enough when applied to broad coverage task typically associated with IR.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ShiGPS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/ShiGPS05,
		author = {Zhongmin Shi and Baohua Gu and Fred Popowich and Anoop Sarkar},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Synonym-Based Expansion and Boosting-Based Re-Ranking: {A} Two-phase Approach for Genomic Information Retrieval},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/simon-fraseru.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ShiGPS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Thresholding Strategies for Text Classifiers: TREC 2005 Biomedical  Triage Task Experiments

_Luo Si, Tapas Kanungo_

- :fontawesome-solid-user-group: **Participant:** [ibm.kanungo](./participants.md#ibm.kanungo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/carnegie-mu-kanungo.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/carnegie-mu-kanungo.geo.pdf)
- :material-file-search: **Runs:** [ABBR003](./runs.md#abbr003) | [ABBR003SThr](./runs.md#abbr003sthr) | [ASVMN03](./runs.md#asvmn03) | [EBBR0006](./runs.md#ebbr0006) | [EBBR0006SThr](./runs.md#ebbr0006sthr) | [ESVMN075](./runs.md#esvmn075) | [GAbsBBR0083](./runs.md#gabsbbr0083) | [GBBR004](./runs.md#gbbr004) | [GSVMN08](./runs.md#gsvmn08) | [TBBR0004](./runs.md#tbbr0004) | [TBBR0004SThr](./runs.md#tbbr0004sthr) | [TSVM0035](./runs.md#tsvm0035)

??? abstract "Abstract"
	
	We participated in the triage task of biomedical documents in the TREC genomic track. In this paper we describe the methods we developed for the four triage1subtasks. Logistic regression and support vector machine algorithms were first trained to generate ranked lists of test documents. Then a subset of the test documents was identified as positive instances by selecting the top-k documents of the ranked lists. Deciding on the ideal value for k requires a good thresholding strategy. In this paper we first describe two thresholding strategies based on i) logistic regression and ii) support vector machines. In addition to these methods, we describe a thresholding method that combines the outputs from logistic regression and support vector machine by applying a joint thresholding strategy.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SiK05.bib) "
	```
	@inproceedings{DBLP:conf/trec/SiK05,
		author = {Luo Si and Tapas Kanungo},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Thresholding Strategies for Text Classifiers: {TREC} 2005 Biomedical Triage Task Experiments},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/carnegie-mu-kanungo.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SiK05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Biomedical Document Triage: Automatic Classification Exploiting Category  Specific Knowledge

_L. Venkata Subramaniam, Sougata Mukherjea, Diwakar Punjani_

- :fontawesome-solid-user-group: **Participant:** [ibm-india.ramakrishnan](./participants.md#ibm-india.ramakrishnan)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/ibm-india.subramaniam.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/ibm-india.subramaniam.geo.pdf)
- :material-file-search: **Runs:** [aIBMIRLsvm](./runs.md#aibmirlsvm) | [aIBMIRLrul](./runs.md#aibmirlrul) | [aIBMIRLmet](./runs.md#aibmirlmet) | [eIBMIRLsvm](./runs.md#eibmirlsvm) | [eIBMIRLrul](./runs.md#eibmirlrul) | [eIBMIRLmet](./runs.md#eibmirlmet) | [gIBMIRLsvm](./runs.md#gibmirlsvm) | [gIBMIRLrul](./runs.md#gibmirlrul) | [gIBMIRLmet](./runs.md#gibmirlmet) | [tIBMIRLsvm](./runs.md#tibmirlsvm) | [tIBMIRLrul](./runs.md#tibmirlrul) | [tIBMIRLmet](./runs.md#tibmirlmet)

??? abstract "Abstract"
	
	We approached the problem of categorizing papers for the 2005 TREC Genomics Track Categorization task in three different ways. In the first, we used a machine learning based approach. We used the MeSH ontology and other specialized ontologies from MGI to identify the set of features to be used in the classification. In the second, for each of the categories, we identified a set of terms to use for filtering the articles. In the third, combined approach, we used the machine learning based approach on the filtered set of articles. In all three approaches we incorporate biological knowledge about the classes into the classification system to achieve improved utility.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SubramaniamMP05.bib) "
	```
	@inproceedings{DBLP:conf/trec/SubramaniamMP05,
		author = {L. Venkata Subramaniam and Sougata Mukherjea and Diwakar Punjani},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Biomedical Document Triage: Automatic Classification Exploiting Category Specific Knowledge},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/ibm-india.subramaniam.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SubramaniamMP05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Enhance Genomic IR with Term Variation and Expansion: Experience  of the IASL Group at Genomic Track 2005

_Tsung-Han Tsai, Chia-Wei Wu, Hsieh-Chuan Hung, Yu-Chun Wang, Ding He, Yi-Feng Lin, Cheng-Wei Lee, Ting-Yi Sung, Wen-Lian Hsu_

- :fontawesome-solid-user-group: **Participant:** [academia.sinica.tsai](./participants.md#academia.sinica.tsai)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/academia-sinica.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/academia-sinica.geo.pdf)
- :material-file-search: **Runs:** [iasl1](./runs.md#iasl1) | [iasl2](./runs.md#iasl2)

??? abstract "Abstract"
	
	The rapid increase of biomedical literature available on the web has made it increasingly difficult to find precise information. To implement an accurate biomedical information retrieval (IR) system, we must deal with the variants of biomedical terms carefully. In this paper, we focus on the generation of aliases, synonyms, acronyms, and lexical variants of such terms. In addition, we also propose a hyphen handling technique for processing hyphenated terms. We use the original terms/phrases, and expanded terms/phrases to construct an Indri query, and evaluate the effectiveness of various methods by two indicators: MAP, and recall. Our experiment results show that tackling hyphenation improves information retrieval significantly. In addition, synonym expansion also enhances IR performance when the focus of a query is identified. For a natural language query, deep semantic analysis and more knowledge-oriented expansion should be applied.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TsaiWHWHLLSH05.bib) "
	```
	@inproceedings{DBLP:conf/trec/TsaiWHWHLLSH05,
		author = {Tsung{-}Han Tsai and Chia{-}Wei Wu and Hsieh{-}Chuan Hung and Yu{-}Chun Wang and Ding He and Yi{-}Feng Lin and Cheng{-}Wei Lee and Ting{-}Yi Sung and Wen{-}Lian Hsu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Enhance Genomic {IR} with Term Variation and Expansion: Experience of the {IASL} Group at Genomic Track 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/academia-sinica.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TsaiWHWHLLSH05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### IIT TREC 2005: Genomics Track

_Jay Urbain, Nazli Goharian, Ophir Frieder_

- :fontawesome-solid-user-group: **Participant:** [iit.urbain](./participants.md#iit.urbain)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/iit-urbain.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/iit-urbain.geo.pdf)
- :material-file-search: **Runs:** [iitprf011003](./runs.md#iitprf011003)

??? abstract "Abstract"
	
	For the TREC-2005 Genomics Track ad-hoc retrieval task, we report on the development of a scalable information retrieval engine based on a relational data model for the integration of structured data and text. Our objectives are to meet the need for the integrated search of heterogeneous data sets of biomedical literature and structured data found in biological databases, and to demonstrate the efficacy of using a relational database for a large biomedical information retrieval application. Utilizing pivoted document normalization (PN) [1], pseudo relevance feedback [2, 3], and without performing stemming or domain specific normalization of biological terms, we received a mean average precision (MAP) of 0.1913 that places our results at the median of 32 Genomics track ad-hoc retrieval participants. Subsequent to our participation in TREC, we have added a new gene/protein term normalization scheme, and have evaluated additional retrieval strategies including: BM25 [15], pivoted unique normalization [1], and language models utilizing absolute discounting, Dirichlet, and Jelinek-Mercer smoothing techniques [12, 13, 16]. With the addition of Porter stemming [17], gene/protein term normalization, and the BM25 probabilistic retrieval strategy, we received a MAP of 0.2879 that places us among the top results for official manual runs reported for the TREC Genomics track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/UrbainGF05.bib) "
	```
	@inproceedings{DBLP:conf/trec/UrbainGF05,
		author = {Jay Urbain and Nazli Goharian and Ophir Frieder},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{IIT} {TREC} 2005: Genomics Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/iit-urbain.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/UrbainGF05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2005 Genomics Track Experiments at DUTAI

_Zhihao Yang, Hongfei Lin, Yanpeng Li, Baoyan Liu, Ye Lu_

- :fontawesome-solid-user-group: **Participant:** [dalianu.yang](./participants.md#dalianu.yang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/dalianu.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/dalianu.geo.pdf)
- :material-file-search: **Runs:** [DUTAdHoc1](./runs.md#dutadhoc1) | [DUTAdHoc2](./runs.md#dutadhoc2) | [aDUTCat1](./runs.md#adutcat1) | [eDUTCat1](./runs.md#edutcat1) | [gDUTCat1](./runs.md#gdutcat1) | [tDUTCat1](./runs.md#tdutcat1) | [aDUTCat2](./runs.md#adutcat2) | [eDUTCat2](./runs.md#edutcat2) | [gDUTCat2](./runs.md#gdutcat2) | [tDUTCat2](./runs.md#tdutcat2)

??? abstract "Abstract"
	
	This paper describes the techniques we applied for the two tasks of the TREC Genomics track, i.e., ad hoc retrieval and categorization tasks. For the ad hoc retrieval task, we used query expansion, different scoring strategy on different parts of Medline record (Title, Abstract, RN, MH, etc.) and pseudo relevance feedback. Our submitted run DUTAdHoc2 obtained a MAP of 0.2349. For the categorization task, our system used a SVM classifier with TFIDF term weighting scheme. In addition concept replacing and filtering methods were adopted. Two of our submitted runs (eDUTCat1 and gDUTCat1) produced a Utility score of 0.8496 and 0.572 respectively ranking third and fourth out of 46 runs submitted for the categorization task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangLLLL05.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangLLLL05,
		author = {Zhihao Yang and Hongfei Lin and Yanpeng Li and Baoyan Liu and Ye Lu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2005 Genomics Track Experiments at {DUTAI}},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/dalianu.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangLLLL05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Genomic Information Retrieval Through Selective Extraction and Tagging  by the ASU-BioAL Group

_Lian Yu, Syed Toufeeq Ahmed, Graciela Gonzalez, Brendan Logsdon, Mutsumi Nakamura, Shawn Nikkila, Kalpesh Shah, Luis Tari, Ryan Wendt, Amanda Zeigler, Chitta Baral_

- :fontawesome-solid-user-group: **Participant:** [arizonau.baral](./participants.md#arizonau.baral)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/arizonasu.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/arizonasu.geo.pdf)
- :material-file-search: **Runs:** [asubaral](./runs.md#asubaral)

??? abstract "Abstract"
	
	In this paper we describe the approach used by the Arizona State University BioAI group for the ad-hoc retrieval task of the TREC Genomics Track 2005. We pre-process TREC query expression by adding the synonyms of genes, diseases, bio-processes, functions of organs, and selectively adding stemming verbs, nouns, and Mesh Heading categories. The pre-processed queries are used to perform initial search on the TREC Genomics collection of MEDLINE abstracts and produce a set of target abstracts using Apache Lucene. Tagging, anaphor resolution and fact extraction are performed on the target abstracts to refine the search results in terms of relevance. Finally, we rank the target abstracts according to the extracted facts, distance between terms and terms appeared in the query.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YuAGLNNSTWZB05.bib) "
	```
	@inproceedings{DBLP:conf/trec/YuAGLNNSTWZB05,
		author = {Lian Yu and Syed Toufeeq Ahmed and Graciela Gonzalez and Brendan Logsdon and Mutsumi Nakamura and Shawn Nikkila and Kalpesh Shah and Luis Tari and Ryan Wendt and Amanda Zeigler and Chitta Baral},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Genomic Information Retrieval Through Selective Extraction and Tagging by the ASU-BioAL Group},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/arizonasu.geo.pdf},
		timestamp = {Wed, 25 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YuAGLNNSTWZB05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2005 Genomics Track at I2R

_Nie Yu, Lingpeng Yang, Dong-Hong Ji, Jie Zhang, Jian Su, Xiaofeng Yang, Soon-Heng Tan, Juan Xiao, Guodong Zhou_

- :fontawesome-solid-user-group: **Participant:** [iir.yu](./participants.md#iir.yu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/inst-infocomm.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/inst-infocomm.geo.pdf)
- :material-file-search: **Runs:** [i2r1](./runs.md#i2r1) | [i2r2](./runs.md#i2r2)

??? abstract "Abstract"
	
	This paper describes the methods we used for the Ad Hoc task of TREC Genomics Track. Synonym dictionary for genes and pseudo relevance feedback are used to expand queries. BM25 model is implemented to retrieve relevant documents. We also tried to exploit name entities and their co-references in the retrieval. Results of submitted runs are listed and discussed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YuYJJSYTXZ05.bib) "
	```
	@inproceedings{DBLP:conf/trec/YuYJJSYTXZ05,
		author = {Nie Yu and Lingpeng Yang and Dong{-}Hong Ji and Jie Zhang and Jian Su and Xiaofeng Yang and Soon{-}Heng Tan and Juan Xiao and Guodong Zhou},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2005 Genomics Track at {I2R}},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/inst-infocomm.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YuYJJSYTXZ05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DataparkSearch at TREC 2005

_Maxim Zakharov_

- :fontawesome-solid-user-group: **Participant:** [datapark.zakharov](./participants.md#datapark.zakharov)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/datapark.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/datapark.geo.pdf)
- :material-file-search: **Runs:** [dpsearch1](./runs.md#dpsearch1) | [dpsearch2](./runs.md#dpsearch2)

??? abstract "Abstract"
	
	This paper describes the experiments of the OOO Datapark in TREC-2005. We participated in the Genomics track and submitted official runs to the Adhoc retrieval task. Our goal is to compare two methods of relevance calculation uses in the DataparkSearch Engine.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Zakharov05.bib) "
	```
	@inproceedings{DBLP:conf/trec/Zakharov05,
		author = {Maxim Zakharov},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {DataparkSearch at {TREC} 2005},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/datapark.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Zakharov05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UIUC/MUSC at TREC 2005 Genomics Track

_ChengXiang Zhai, Xu Ling, Xin He, Atulya Velivelli, Xuanhui Wang, Hui Fang, Azadeh Shakery, Xinghua Lu_

- :fontawesome-solid-user-group: **Participant:** [uiuc.zhai](./participants.md#uiuc.zhai)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uillinois-uc.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/uillinois-uc.geo.pdf)
- :material-file-search: **Runs:** [UIUCgAuto](./runs.md#uiucgauto) | [UIUCgInt](./runs.md#uiucgint) | [aMUSCUIUC1](./runs.md#amuscuiuc1) | [aMUSCUIUC2](./runs.md#amuscuiuc2) | [aMUSCUIUC3](./runs.md#amuscuiuc3) | [eMUSCUIUC1](./runs.md#emuscuiuc1) | [eMUSCUIUC2](./runs.md#emuscuiuc2) | [eMUSCUIUC3](./runs.md#emuscuiuc3) | [gMUSCUIUC1](./runs.md#gmuscuiuc1) | [gMUSCUIUC2](./runs.md#gmuscuiuc2) | [gMUSCUIUC3](./runs.md#gmuscuiuc3) | [tMUSCUIUC1](./runs.md#tmuscuiuc1) | [tMUSCUIUC2](./runs.md#tmuscuiuc2) | [tMUSCUIUC3](./runs.md#tmuscuiuc3)

??? abstract "Abstract"
	
	We report experiment results from the collaborative participation of UIUC and MUSC in the TREC 2005 Genomics Track. We participated in both the adhoc task and the categorization task, and studied the use of some mixture language models in these tasks. Experiment results show that a structured theme-based language modeling approach is effective in improving retrieval effectiveness for the ad hoc taks and the Latent Dirichlet Allocation method is effective in dimension reduction for the categorization task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhaiLHVWFSL05.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhaiLHVWFSL05,
		author = {ChengXiang Zhai and Xu Ling and Xin He and Atulya Velivelli and Xuanhui Wang and Hui Fang and Azadeh Shakery and Xinghua Lu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UIUC/MUSC} at {TREC} 2005 Genomics Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uillinois-uc.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhaiLHVWFSL05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Applying Probabilistic Thematic Clustering for Classification in the  TREC 2005 Genomics Track

_Z. H. Zheng, Scott Brady, Akash Garg, Hagit Shatkay_

- :fontawesome-solid-user-group: **Participant:** [queensu.shatkay](./participants.md#queensu.shatkay)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/queensu.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/queensu.geo.pdf)
- :material-file-search: **Runs:** [aQUNB8](./runs.md#aqunb8) | [aQUT11](./runs.md#aqut11) | [aQUT14](./runs.md#aqut14) | [eQUNB11](./runs.md#equnb11) | [eQUNB19](./runs.md#equnb19) | [eQUT18](./runs.md#equt18) | [gQUNB12](./runs.md#gqunb12) | [gQUNB15](./runs.md#gqunb15) | [gQUT22](./runs.md#gqut22) | [tQUNB3](./runs.md#tqunb3) | [tQUT10](./runs.md#tqut10) | [tQUT14](./runs.md#tqut14)

??? abstract "Abstract"
	
	Our group participated in the categorization task of the TREC Genomics Track. We introduced and investigated a cluster-based approach for classifying documents. We first clustered the abstracts of the negative training examples based on their term distribution, then built a classifier to distinguish between each cluster and the set of positive examples. The large number of resulting classifiers (a total of 14-19 classifiers per domain) was combined to categorize the test set. We also conducted experiments for cluster-based feature selection; Rather than select features from the whole negative and positive training sets, we selected features from each of the clusters and took the union of these features as the selected features for representing the whole training and test data. We compared our cluster-based multi-classifier approach against a simple naïve Bayes classification. We also compared the cluster-based feature selection strategy with the commonly used Chi-square-based feature selection.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhengBGS05.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhengBGS05,
		author = {Z. H. Zheng and Scott Brady and Akash Garg and Hagit Shatkay},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Applying Probabilistic Thematic Clustering for Classification in the {TREC} 2005 Genomics Track},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/queensu.geo.pdf},
		timestamp = {Mon, 17 Apr 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/ZhengBGS05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiment Report of TREC 2005 Genomics Track ad hoc Retrieval Task

_Wei Zhou, Clement T. Yu_

- :fontawesome-solid-user-group: **Participant:** [uillinois-chicago.liu](./participants.md#uillinois-chicago.liu)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec14/papers/uillinois-chicago.geo.pdf](http://trec.nist.gov/pubs/trec14/papers/uillinois-chicago.geo.pdf)
- :material-file-search: **Runs:** [UICgen1](./runs.md#uicgen1)

??? abstract "Abstract"
	
	This report describes the experiments we have conducted on the ad hoc retrieval task of Genomics track at TREC 2005. In the experiment, a number of different techniques were employed, including Porter stemming, MeSH term and gene name identification, Okapi, weighting schemes, query expansion, and concept-based ranking strategy. The results on sample topics are reported. Future improvements, such as utilizing domain-specific knowledge, gene name disambiguation, and pseudo-feedback are discussed.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhouY05.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhouY05,
		author = {Wei Zhou and Clement T. Yu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiment Report of {TREC} 2005 Genomics Track ad hoc Retrieval Task},
		booktitle = {Proceedings of the Fourteenth Text REtrieval Conference, {TREC} 2005, Gaithersburg, Maryland, USA, November 15-18, 2005},
		series = {{NIST} Special Publication},
		volume = {500-266},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2005},
		url = {http://trec.nist.gov/pubs/trec14/papers/uillinois-chicago.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhouY05.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

