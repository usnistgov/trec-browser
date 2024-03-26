# Proceedings - Genomics 2004 

#### TREC 2004 Genomics Track Overview

_William R. Hersh, Ravi Teja Bhupatiraju, L. Ross, Aaron M. Cohen, Dale Kraemer, Phoebe Johnson_

- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/GEO.OVERVIEW.pdf](http://trec.nist.gov/pubs/trec13/papers/GEO.OVERVIEW.pdf)
??? abstract "Abstract"
	
	The TREC 2004 Genomics Track consisted of two tasks. The first task was a standard ad hoc retrieval task using topics obtained from real biomedical research scientists and documents from a large subset of the MEDLINE bibliographic database. The second task focused on categorization of full-text documents, simulating the task of curators of the Mouse Genome Informatics (MGI) system and consisting of three subtasks. One subtask focused on the triage of articles likely to have experimental evidence warranting the assignment of GO terms, while the other two subtasks focused on the assignment of the three top-level GO categories. The track had 33 participating groups.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HershBRCKJ04.bib) "
	```
	@inproceedings{DBLP:conf/trec/HershBRCKJ04,
		author = {William R. Hersh and Ravi Teja Bhupatiraju and L. Ross and Aaron M. Cohen and Dale Kraemer and Phoebe Johnson},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2004 Genomics Track Overview},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/GEO.OVERVIEW.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/HershBRCKJ04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Knowledge-Intensive and Statistical Approaches to the Retrieval and  Annotation of Genomics MEDLINE Citations

_Alan R. Aronson, Susanne M. Humphrey, Nicholas C. Ide, Won Kim, Russell F. Loane, James G. Mork, Lawrence H. Smith, Lorraine K. Tanabe, W. John Wilbur, Natalie Xie, Dina Demner-Fushman, Hongfang Liu_

- :fontawesome-solid-user-group: **Participant:** [nlm.umd.ul](./participants.md#nlm.umd.ul)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/nlm-umd-ul.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/nlm-umd-ul.geo.pdf)
- :material-file-search: **Runs:** [LHCUMDSE](./runs.md#lhcumdse) | [tq0](./runs.md#tq0) | [NLMT21](./runs.md#nlmt21) | [NLMT22](./runs.md#nlmt22) | [NLMT2ADA](./runs.md#nlmt2ada) | [NLMT2BAYES](./runs.md#nlmt2bayes) | [NLMT2SVM](./runs.md#nlmt2svm) | [NLMA1](./runs.md#nlma1) | [NLMA2](./runs.md#nlma2)

??? abstract "Abstract"
	
	Retrieving and annotating relevant information sources in the genomics literature are difficult but common tasks undertaken by biologists. The research presented here addresses these issues by exploring methods for retrieving MEDLINE® citations that answer real biologists' information needs and by addressing the initial tasks required to annotate MEDLINE citations having genomic content with terms from the Gene Ontology (GO). We approached the retrieval task using two methods: aggressive, knowledge-intensive query expansion and text neighboring. Our approaches to the triage subtask for annotation consisted of traditional machine learning (ML) methods as well as a novel ML algorithm for thematic analysis. Finally, we used a statistical, n-gram heuristic to decide which of the GO hierarchies should be used to annotate a given MEDLINE citation.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/AronsonHIKLMSTWXDL04.bib) "
	```
	@inproceedings{DBLP:conf/trec/AronsonHIKLMSTWXDL04,
		author = {Alan R. Aronson and Susanne M. Humphrey and Nicholas C. Ide and Won Kim and Russell F. Loane and James G. Mork and Lawrence H. Smith and Lorraine K. Tanabe and W. John Wilbur and Natalie Xie and Dina Demner{-}Fushman and Hongfang Liu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Knowledge-Intensive and Statistical Approaches to the Retrieval and Annotation of Genomics {MEDLINE} Citations},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/nlm-umd-ul.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/AronsonHIKLMSTWXDL04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Expanding Queries Using Stems and Symbols

_Michela Bacchin, Massimo Melucci_

- :fontawesome-solid-user-group: **Participant:** [u.padova](./participants.md#u.padova)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/upadova.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/upadova.geo.pdf)
- :material-file-search: **Runs:** [PDTNsmp4](./runs.md#pdtnsmp4) | [PD50501](./runs.md#pd50501)

??? abstract "Abstract"
	
	This paper describes the experiments conducted in the ad-hoc retrieval task of the Genomic track at TREC 2004. Different query expansion techniques based on the addition of keyword stems and of genomic product symbols selected by relevance feedback were studied. Stemming was tested using a mutual reinforcement process for building a domain-specific stemmer. Relevance feedback was tested using a technique exploiting associations between symbols and related keywords.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BacchinM04.bib) "
	```
	@inproceedings{DBLP:conf/trec/BacchinM04,
		author = {Michela Bacchin and Massimo Melucci},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Expanding Queries Using Stems and Symbols},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/upadova.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BacchinM04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### RMIT University at TREC 2004

_Bodo Billerbeck, Adam Cannane, Abhijit Chattaraj, Nicholas Lester, William Webber, Hugh E. Williams, John Yiannis, Justin Zobel_

- :fontawesome-solid-user-group: **Participant:** [rmit.scholer](./participants.md#rmit.scholer)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/rmit.tera.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/rmit.tera.geo.pdf)
- :material-file-search: **Runs:** [RMITa](./runs.md#rmita) | [RMITb](./runs.md#rmitb)

??? abstract "Abstract"
	
	RMIT University participated in two tracks at TREC 2004: Terabyte and Genomics, both for the first time. This paper describes the techniques we applied and our experiments in both tracks, and discusses the results of the genomics track runs; the terabyte track results are unavailable at the time of manuscript submission. We also describe our new zettair search engine, in use for the first time at TREC.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BillerbeckCCLWWYZ04.bib) "
	```
	@inproceedings{DBLP:conf/trec/BillerbeckCCLWWYZ04,
		author = {Bodo Billerbeck and Adam Cannane and Abhijit Chattaraj and Nicholas Lester and William Webber and Hugh E. Williams and John Yiannis and Justin Zobel},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{RMIT} University at {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/rmit.tera.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BillerbeckCCLWWYZ04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experiments in Terabyte Searching, Genomic Retrieval and Novelty Detection  for TREC 2004

_Stephen Blott, Fabrice Camous, Paul Ferguson, Georgina Gaughan, Cathal Gurrin, Gareth J. F. Jones, Noel Murphy, Noel E. O'Connor, Alan F. Smeaton, Peter Wilkins, Oisín Boydell, Barry Smyth_

- :fontawesome-solid-user-group: **Participant:** [dubblincity.u](./participants.md#dubblincity.u)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/dcu.tera.geo.novelty.pdf](http://trec.nist.gov/pubs/trec13/papers/dcu.tera.geo.novelty.pdf)
- :material-file-search: **Runs:** [DCUma](./runs.md#dcuma) | [DCUmatn1](./runs.md#dcumatn1)

??? abstract "Abstract"
	
	In TREC2004, Dublin City University took part in three tracks, Terabyte (in collaboration with University College Dublin), Genomic and Novelty. In this paper we will discuss each track separately and present separate conclusions from this work. In addition, we present a general description of a text retrieval engine that we have developed in the last year to support our experiments into large scale, distributed information retrieval, which underlies all of the track experiments described in this document.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/BlottCFGGJMOSWBS04.bib) "
	```
	@inproceedings{DBLP:conf/trec/BlottCFGGJMOSWBS04,
		author = {Stephen Blott and Fabrice Camous and Paul Ferguson and Georgina Gaughan and Cathal Gurrin and Gareth J. F. Jones and Noel Murphy and Noel E. O'Connor and Alan F. Smeaton and Peter Wilkins and Ois{\'{\i}}n Boydell and Barry Smyth},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experiments in Terabyte Searching, Genomic Retrieval and Novelty Detection for {TREC} 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/dcu.tera.geo.novelty.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/BlottCFGGJMOSWBS04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Domain-Specific Synonym Expansion and Validation for Biomedical Information  Retrieval (MultiText Experiments for TREC 2004)

_Stefan Büttcher, Charles L. A. Clarke, Gordon V. Cormack_

- :fontawesome-solid-user-group: **Participant:** [u.waterloo.clarke](./participants.md#u.waterloo.clarke)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/uwaterloo-clarke.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/uwaterloo-clarke.geo.pdf)
- :material-file-search: **Runs:** [uwmtDg04tn](./runs.md#uwmtdg04tn) | [uwmtDg04n](./runs.md#uwmtdg04n)

??? abstract "Abstract"
	
	In the domain of biomedical publications, synonyms and homonyms are omnipresent and pose a great challenge for document retrieval systems. For this year's TREC Genomics Ad hoc Retrieval Task, we mainly addressed the problem of dealing with synonyms. We examined the impact of domain-specific knowledge on the effectiveness of query expansion and analyzed the quality of Google as a source of query expansion terms based on pseudo-relevance feedback. Our results show that automatic acronym expansion, realized by querying the AcroMed database of biomedical acronyms, almost always improves the performance of our document retrieval system. Google, on the other hand, produced results that were worse than the other, corpus-based feedback techniques we used as well in our experiments. We believe that the primary reason for Google's bad performance in this task is its highly restricted query language.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ButtcherCC04.bib) "
	```
	@inproceedings{DBLP:conf/trec/ButtcherCC04,
		author = {Stefan B{\"{u}}ttcher and Charles L. A. Clarke and Gordon V. Cormack},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Domain-Specific Synonym Expansion and Validation for Biomedical Information Retrieval (MultiText Experiments for {TREC} 2004)},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/uwaterloo-clarke.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ButtcherCC04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Phrasal Queries with LingPipe and Lucene: Ad Hoc Genomics Text Retrieval

_Bob Carpenter_

- :fontawesome-solid-user-group: **Participant:** [alias-i](./participants.md#alias-i)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/alias-i.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/alias-i.geo.pdf)
- :material-file-search: **Runs:** [aliasiTerms](./runs.md#aliasiterms) | [aliasiBase](./runs.md#aliasibase)

??? abstract "Abstract"
	
	The hypothesis we explored for the Ad Hoc task of the Genomics track for TREC 2004 was that phrase-level queries would increase precision over a baseline of token-level terms. We implemented our approach using two open source tools: the Apache Jakarta Lucene TF/IDF search engine (version 1.3) and the Alias-i LingPipe tokenizer and named-entity annotator (version 1.0.6). Contrary to our intuitions, the baseline system provided better performance in terms of recall and precision for almost every query at almost every precision/recall operating point.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Carpenter04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Carpenter04,
		author = {Bob Carpenter},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Phrasal Queries with LingPipe and Lucene: Ad Hoc Genomics Text Retrieval},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/alias-i.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Carpenter04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Feature Generation, Feature Selection, Classifiers, and Conceptual  Drift for Biomedical Document Triage

_Aaron M. Cohen, Ravi Teja Bhupatiraju, William R. Hersh_

- :fontawesome-solid-user-group: **Participant:** [ohsu.hersh](./participants.md#ohsu.hersh)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/ohsu-hersh.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/ohsu-hersh.geo.pdf)
- :material-file-search: **Runs:** [OHSUAll](./runs.md#ohsuall) | [OHSUNeeds](./runs.md#ohsuneeds) | [OHSUNBAYES](./runs.md#ohsunbayes) | [OHSUSVMJ20](./runs.md#ohsusvmj20) | [OHSUVP](./runs.md#ohsuvp)

??? abstract "Abstract"
	
	We approached the problem of classifying papers for the TREC 2004 Genomics Track triage task as a four step process: feature generation, feature selection, classifier training, and finally, classification. Section specific binary features that discriminated significantly between positive and negative training samples were chosen using the Chi-square statistic. Three classifiers were trained on this feature set: a simple Naive Bayes classifier, the SVMLight support vector machine implementation, and a voting perceptron extended to support variable learning rates. Comparing the classifiers on the training data we found that neither Naive Bayes nor SVMLight was able to adequately account for the factor of 20 in the utility function. The voting perceptron classifier performed much better at this. The performance on the test collection was lower for all classifiers, although consistent with the relative values of the training cross-validation. Feature subsetting showed no significant differences in precision or recall, implying that there was some redundancy among the features. We also examined how well the feature set derived from the 2002 training collection represented the papers in the 2003 test collection, and found a low level of similarity between feature sets derived from the two collections. This supports the hypothesis that important classification terms change quickly over time.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CohenBH04.bib) "
	```
	@inproceedings{DBLP:conf/trec/CohenBH04,
		author = {Aaron M. Cohen and Ravi Teja Bhupatiraju and William R. Hersh},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Feature Generation, Feature Selection, Classifiers, and Conceptual Drift for Biomedical Document Triage},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/ohsu-hersh.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CohenBH04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Concept Extraction and Synonymy Management for Biomedical Information  Retrieval

_Colleen E. Crangle, Alex Zbyslaw, J. Michael Cherry, Eurie L. Hong_

- :fontawesome-solid-user-group: **Participant:** [converspeech](./participants.md#converspeech)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/converspeech.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/converspeech.geo.pdf)
- :material-file-search: **Runs:** [ConversAuto](./runs.md#conversauto) | [ConversManu](./runs.md#conversmanu)

??? abstract "Abstract"
	
	This paper reports on work done for the Genomics Track at TREC 2004 by ConverSpeech LLC in conjunction with scientists at the Saccharomyces Genome Database (SGD), the model organism database located at Stanford University, California. The rapidly increasing number of articles in the biomedical literature has created new urgency for software tools that find information relevant to specific information needs. We focused on two challenges in this work: the problems of synonymy (several terms having the same meaning) and polysemy (a term having more than one meaning), and the problem of constructing queries from information needs stated in natural language. We investigated the use of concept extraction for the second problem, relying on the limited statements of information need as the source of textual analysis. To minimize the problem of synonymy, we investigated the use of a language-oriented biomedical ontology and MeSH (Medical Subject Headings) for term expansion. Additionally, to minimize the problem of polysemy, we used extracted concepts to analyze and rank the documents returned by a search. We submitted two sets of results to TREC for evaluation, the first one produced automatically, the second derived from the first by making specific kinds of changes in the query and ranking methods. The mean average precision (MAP) for the automatic result was lower than the median of the 37 submitted runs overall; however, desirable results were obtained for mean average precision at 10 and 100 documents for almost half the topics. The MAP for the derived result was higher than the median, a desirable result.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/CrangleZCH04.bib) "
	```
	@inproceedings{DBLP:conf/trec/CrangleZCH04,
		author = {Colleen E. Crangle and Alex Zbyslaw and J. Michael Cherry and Eurie L. Hong},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Concept Extraction and Synonymy Management for Biomedical Information Retrieval},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/converspeech.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/CrangleZCH04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### The GUC Goes to TREC 2004: Using Whole or Partial Documents for  Retrieval and Classification in the Genomics Track

_Kareem Darwish, Amgad Madkour_

- :fontawesome-solid-user-group: **Participant:** [german.u.cairo](./participants.md#german.u.cairo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/german.u.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/german.u.geo.pdf)
- :material-file-search: **Runs:** [PSE](./runs.md#pse) | [GUClin1700](./runs.md#guclin1700) | [GUClin1260](./runs.md#guclin1260) | [GUCply1260](./runs.md#gucply1260) | [GUCply1700](./runs.md#gucply1700) | [GUCwdply2000](./runs.md#gucwdply2000) | [GUCbase](./runs.md#gucbase) | [GUCsvm0](./runs.md#gucsvm0) | [GUCsvm5](./runs.md#gucsvm5) | [GUCir30](./runs.md#gucir30) | [GUCir50](./runs.md#gucir50)

??? abstract "Abstract"
	
	We were interested in examining the relative effect of using parts of the documents, different combinations of parts of the documents, or whole documents on retrieval and classification. We were also interested in the effect of MeSH terms on retrieval. Our experiments show that indexing titles, abstracts, and MeSH terms for adhoc retrieval yielded statistically significantly better results than any other part or combination of parts, with abstracts outperforming any other individual part of the documents. In the triage sub-task, using whole documents for training a classifier outperformed using titles, abstracts, diagram captions, MeSH terms, and windows of text around gene names. However, training a classifier using the combination of titles, abstracts, and MeSH terms produced results comparable to using whole documents.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DarwishM04.bib) "
	```
	@inproceedings{DBLP:conf/trec/DarwishM04,
		author = {Kareem Darwish and Amgad Madkour},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {The {GUC} Goes to {TREC} 2004: Using Whole or Partial Documents for Retrieval and Classification in the Genomics Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/german.u.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DarwishM04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### DIMACS at the TREC 2004 Genomics Track

_Aynur A. Dayanik, Dmitriy Fradkin, Alexander Genkin, Paul B. Kantor, David Madigan, David D. Lewis, Vladimir Menkov_

- :fontawesome-solid-user-group: **Participant:** [rutgers.dayanik](./participants.md#rutgers.dayanik)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/rutgers-dayanik.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/rutgers-dayanik.geo.pdf)
- :material-file-search: **Runs:** [rutgersGAH1](./runs.md#rutgersgah1) | [rutgersGAH2](./runs.md#rutgersgah2) | [dimacsAabsw1](./runs.md#dimacsaabsw1) | [dimacsAp5w5](./runs.md#dimacsap5w5) | [dimacsAw20w5](./runs.md#dimacsaw20w5) | [dimacsTfl9d](./runs.md#dimacstfl9d) | [dimacsTfl9w](./runs.md#dimacstfl9w) | [dimacsTl9md](./runs.md#dimacstl9md) | [dimacsTl9mhg](./runs.md#dimacstl9mhg) | [dimacsTl9w](./runs.md#dimacstl9w) | [dimacsAl3w](./runs.md#dimacsal3w) | [dimacsAg3mh](./runs.md#dimacsag3mh)

??? abstract "Abstract"
	
	DIMACS participated in the text categorization and ad hoc retrieval tasks of the TREC 2004 Genomics track. For the categorization task, we tackled the triage and annotation hierarchy subtasks.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/DayanikFGKMLM04.bib) "
	```
	@inproceedings{DBLP:conf/trec/DayanikFGKMLM04,
		author = {Aynur A. Dayanik and Dmitriy Fradkin and Alexander Genkin and Paul B. Kantor and David Madigan and David D. Lewis and Vladimir Menkov},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{DIMACS} at the {TREC} 2004 Genomics Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/rutgers-dayanik.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/DayanikFGKMLM04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Novelty, Question Answering and Genomics: The University of Iowa Response

_David Eichmann, Yi Zhang, Shannon Bradshaw, Xin Ying Qiu, Li Zhou, Padmini Srinivasan, Aditya Kumar Sehgal, Hudon Wong_

- :fontawesome-solid-user-group: **Participant:** [u.iowa](./participants.md#u.iowa)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/uiowa.novelty.qa.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/uiowa.novelty.qa.geo.pdf)
- :material-file-search: **Runs:** [UIowaGN1](./runs.md#uiowagn1) | [iowarun1](./runs.md#iowarun1) | [iowarun2](./runs.md#iowarun2) | [iowarun3](./runs.md#iowarun3) | [iowarun4](./runs.md#iowarun4)

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/EichmannZBQZSSW04.bib) "
	```
	@inproceedings{DBLP:conf/trec/EichmannZBQZSSW04,
		author = {David Eichmann and Yi Zhang and Shannon Bradshaw and Xin Ying Qiu and Li Zhou and Padmini Srinivasan and Aditya Kumar Sehgal and Hudon Wong},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Novelty, Question Answering and Genomics: The University of Iowa Response},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/uiowa.novelty.qa.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/EichmannZBQZSSW04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Revisiting Again Document Length Hypotheses TREC 2004 Genomics Track  Experiments at Patolis

_Sumio Fujita_

- :fontawesome-solid-user-group: **Participant:** [patolis.fujita](./participants.md#patolis.fujita)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/patolis.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/patolis.geo.pdf)
- :material-file-search: **Runs:** [pllsgen4a1](./runs.md#pllsgen4a1) | [pllsgen4a2](./runs.md#pllsgen4a2) | [pllsgen4t1](./runs.md#pllsgen4t1) | [pllsgen4t2](./runs.md#pllsgen4t2) | [pllsgen4t3](./runs.md#pllsgen4t3) | [pllsgen4t4](./runs.md#pllsgen4t4) | [pllsgen4t5](./runs.md#pllsgen4t5)

??? abstract "Abstract"
	
	The TREC-2004 Genomics track evaluation experiments at Patolis Corporation are described with a focus on the document length issues in different retrieval models such as TF*IDF or probabilistic language modeling approaches. In the genomics ad hoc retrieval task, combination of pseudo-relevance feedback and reference database feedback is applied. For the triage sub-task, we trained a SVM classifier using leave-one-out-cross-validation, and calibrated parameters to be optimal against the training set.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Fujita04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Fujita04,
		author = {Sumio Fujita},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Revisiting Again Document Length Hypotheses {TREC} 2004 Genomics Track Experiments at Patolis},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/patolis.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Fujita04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Categorization of Genomics Text Based on Decision Rules

_Rocio Guillén_

- :fontawesome-solid-user-group: **Participant:** [u.sanmarcos](./participants.md#u.sanmarcos)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/cal-state-sanmarcos.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/cal-state-sanmarcos.geo.pdf)
- :material-file-search: **Runs:** [csusm](./runs.md#csusm) | [TRICSUSM](./runs.md#tricsusm)

??? abstract "Abstract"
	
	In this paper we present the approach, experiments and results for the categorization task in the Genomics Track. The approach we used is based on decision trees and decision rules for text categorization 1, 2, 3. The features selected were the keywords and the contents of the glosref tags to induce rules. Rules were then matched with the contents of font-changes in the abstracts of the documents to determine whether to select or not the text.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Guillen04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Guillen04,
		author = {Rocio Guill{\'{e}}n},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Categorization of Genomics Text Based on Decision Rules},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/cal-state-sanmarcos.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Guillen04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Sheffield University and the TREC 2004 Genomics Track: Query Expansion  Using Synonymous Terms

_Yikun Guo, Henk Harkema, Robert J. Gaizauskas_

- :fontawesome-solid-user-group: **Participant:** [u.sheffield.gaizauskas](./participants.md#u.sheffield.gaizauskas)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/usheffield.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/usheffield.geo.pdf)
- :material-file-search: **Runs:** [shefauto1](./runs.md#shefauto1) | [shefauto2](./runs.md#shefauto2)

??? abstract "Abstract"
	
	In this paper we describe our approach to the Ad Hoc Retrieval task of the TREC 2004 Genomics Track. This is a conventional searching task based on a 10-year subset of MEDLINE (about 4.5 million documents and 9 gigabytes in size) and 50 topics derived from information needs obtained via interviews of real biomedical researchers. We will also discuss the results of our submitted runs. The hypothesis we want to test is whether the performance on this particular retrieval task can be improved by expanding queries with synonyms of the original query terms. We use the UMLS Metathesaurus, a comprehensive collection of controlled vocabularies in the biomedical domain, to identify query terms in topics and to determine their synonyms. Our approach is simple in the sense that we only consider synonyms of query terms and do not exploit hierarchical relations between terms such as hyponomy and hyperonymy. Synonymy-based query expansion generally increases recall, but decreases precision due to ambiguous terms. Word senses of ambiguous terms which are inappropriate with regard to the topic under consideration give rise to “polluting” synonyms. We hope that the use of a specifically biomedical term resource such as UMLS will limit the negative effects synonymy-based query expansion may have on precision.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/GuoHG04.bib) "
	```
	@inproceedings{DBLP:conf/trec/GuoHG04,
		author = {Yikun Guo and Henk Harkema and Robert J. Gaizauskas},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Sheffield University and the {TREC} 2004 Genomics Track: Query Expansion Using Synonymous Terms},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/usheffield.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/GuoHG04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### York University at TREC 2004: HARD and Genomics Tracks

_Xiangji Huang, Yan Rui Huang, Ming Zhong, Miao Wen_

- :fontawesome-solid-user-group: **Participant:** [york.u](./participants.md#york.u)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/yorku.hard.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/yorku.hard.geo.pdf)
- :material-file-search: **Runs:** [york04g2](./runs.md#york04g2) | [york04g1](./runs.md#york04g1)

??? abstract "Abstract"
	
	York University participated in HARD and Genomics tracks this year. For both tracks, we used Okapi BSS (basic search system) as the basis. Our experiments mainly focused on exploiting various methods for combining document and passage scores, new term weighting formulae and feedback methods for query expansion. For HARD track, we built two levels of indexes, and search against both indexes for each topic. Then we combine these two searches into one. For Genomics track, we used a new strategy to automatically expand search terms by using relevance feedback and combined retrieval results from different fields into the final result. We achieved good results on the HARD task and average results on the Genomics task. For the HARD passage level evaluation, the automatic run 'yorku04ha1' obtained the best result (0.358) in terms of Bpref measure at 12K characters. The evaluation results show that Algorithm 1 is more effective than Algorithm 2 for the passage level retrieval.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/HuangHZW04.bib) "
	```
	@inproceedings{DBLP:conf/trec/HuangHZW04,
		author = {Xiangji Huang and Yan Rui Huang and Ming Zhong and Miao Wen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {York University at {TREC} 2004: {HARD} and Genomics Tracks},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/yorku.hard.geo.pdf},
		timestamp = {Tue, 05 Sep 2023 01:00:00 +0200},
		biburl = {https://dblp.org/rec/conf/trec/HuangHZW04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### MeSH Based Feedback, Concept Recognition and Stacked Classification  for Curation Tasks

_Wessel Kraaij, Stephan Raaijmakers, Marc Weeber, Rob Jelier_

- :fontawesome-solid-user-group: **Participant:** [tno.kraaij](./participants.md#tno.kraaij)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/tno-emc.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/tno-emc.geo.pdf)
- :material-file-search: **Runs:** [tnog2](./runs.md#tnog2) | [tnog3](./runs.md#tnog3) | [EMCTNOT1](./runs.md#emctnot1)

??? abstract "Abstract"
	
	This paper reports about experiments carried out in the context of the genomics track at TREC 2004. Experiments were concentrated on two subtasks: the ad hoc retrieval task and the triage task. Experiments for the ad hoc task aimed at improving a standard full-text ad-hoc run (using a language modeling approach) by exploiting the manual classification of MEDLINE abstracts (the MeSH terms) for relevance feedback. The triage task was modeled as a standard classification task, using stacked classifiers and complex features, recognized by the Collexis IR engine.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/KraaijRWJ04.bib) "
	```
	@inproceedings{DBLP:conf/trec/KraaijRWJ04,
		author = {Wessel Kraaij and Stephan Raaijmakers and Marc Weeber and Rob Jelier},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {MeSH Based Feedback, Concept Recognition and Stacked Classification for Curation Tasks},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/tno-emc.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/KraaijRWJ04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Identifying Relevant Full-Text Articles for GO Annotation Without  MeSH Terms

_Chih Lee, Wen-Juan Hou, Hsin-Hsi Chen_

- :fontawesome-solid-user-group: **Participant:** [ntu.chen](./participants.md#ntu.chen)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/ntu.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/ntu.geo.pdf)
- :material-file-search: **Runs:** [NTU2v3N1](./runs.md#ntu2v3n1) | [NTU3v3N1](./runs.md#ntu3v3n1) | [NTU3v3N1c2](./runs.md#ntu3v3n1c2) | [NTU4v3N1416](./runs.md#ntu4v3n1416)

??? abstract "Abstract"
	
	Gene Ontology (GO) is a controlled vocabulary. Given a gene product, GO enables scientists to clearly and unambiguously describe specific molecular functions of the gene product, specific biological processes in which it is involved, and specific cellular components to which it is localized. In this paper, we present our approach to identifying which papers have experimental evidence warranting annotation with GO codes. The training data set contains 375 relevant full-text articles and 5,462 irrelevant ones, and the test data set contains 420 positive full-text articles and 5,623 negative ones. We regarded this problem as a binary classification problem, and employed Support Vector Machines (SVMs) to distinguish positive articles from negative ones. Title, abstract, figure/table captions, and three standard sections - Results, Discussion, and Conclusion were the targets of feature extraction. Without incorporating MeSH (Medical Subject Headings) terms as part of the features, our system achieved 0.381 in Normalized Utility measure.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LeeHC04.bib) "
	```
	@inproceedings{DBLP:conf/trec/LeeHC04,
		author = {Chih Lee and Wen{-}Juan Hou and Hsin{-}Hsi Chen},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Identifying Relevant Full-Text Articles for {GO} Annotation Without MeSH Terms},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/ntu.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LeeHC04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### THUIR at TREC 2004: Genomics Track

_Jiao Li, Xian Zhang, Min Zhang, Xiaoyan Zhu_

- :fontawesome-solid-user-group: **Participant:** [tsinghua.ma](./participants.md#tsinghua.ma)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/tsinghua-ma.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/tsinghua-ma.geo.pdf)
- :material-file-search: **Runs:** [THUIRgen01](./runs.md#thuirgen01) | [THUIRgen02](./runs.md#thuirgen02) | [THIRcat01](./runs.md#thircat01) | [THIRcat02](./runs.md#thircat02) | [THIRcat03](./runs.md#thircat03) | [THIRcat04](./runs.md#thircat04) | [THIRcat05](./runs.md#thircat05)

??? abstract "Abstract"
	
	This is the first time that THUIR participates in TREC Genomics Track. We took part in both Ad hoc retrieval task and Categorization task. Based on our retrieval system TMiner, our research in the Ad hoc retrieval task focuses on: (1) Category of organism retrieval strategy; (2) Primary Feature Model; (3) Query Expansion (QE) technology; (4) Result fusion method. Five official runs have been submitted at triage task in the Categorization task. Unigrams are used as features in Vector Space Model, and the high dimension feature vectors are trained and classified by SVM classifier with RBFs as the kernel function. Three ways are taken to improve the classifier: (1) Perform feature selection to reduce the dimension of feature vectors; (2) Weight the important features; (3) Balance between the positive dataset and the negative dataset.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/LiZZZ04.bib) "
	```
	@inproceedings{DBLP:conf/trec/LiZZZ04,
		author = {Jiao Li and Xian Zhang and Min Zhang and Xiaoyan Zhu},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{THUIR} at {TREC} 2004: Genomics Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/tsinghua-ma.geo.pdf},
		timestamp = {Wed, 02 Nov 2022 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/LiZZZ04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### BioText Team Experiments for the TREC 2004 Genomics Track

_Preslav Nakov, Ariel S. Schwartz, Emilia Stoica, Marti A. Hearst_

- :fontawesome-solid-user-group: **Participant:** [u.hospital.geneva](./participants.md#u.hospital.geneva)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/ucal-berkeley.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/ucal-berkeley.geo.pdf)
- :material-file-search: **Runs:** [geneteam1](./runs.md#geneteam1) | [geneteam2](./runs.md#geneteam2) | [geneteam3](./runs.md#geneteam3) | [geneteamA1](./runs.md#geneteama1) | [geneteamA2](./runs.md#geneteama2) | [geneteamA3](./runs.md#geneteama3) | [geneteamA4](./runs.md#geneteama4) | [geneteamA5](./runs.md#geneteama5)

??? abstract "Abstract"
	
	The BioText group participated in the two main tasks of the TREC 2004 Genomics track. Our approach to the ad hoc task was similar to the one used in the 2003 Genomics track, but due to the lack of training data, we did not achieve the high scores of the previous year. The most novel aspect of our submission for the categorization task centers around our method for assigning Gene Ontology (GO) codes to articles marked for curation. This approach compares the text surrounding a target gene to text that has been found to be associated with GO codes assigned to homologous genes for organisms with genomes similar to mice (namely, humans and rats). We applied the same method to GO codes that have been assigned to MGI entries in years prior to the test set. In addition, we filtered out proposed GO codes based on their previously observed likelihood to co-occur with one another.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/NakovSSH04.bib) "
	```
	@inproceedings{DBLP:conf/trec/NakovSSH04,
		author = {Preslav Nakov and Ariel S. Schwartz and Emilia Stoica and Marti A. Hearst},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {BioText Team Experiments for the {TREC} 2004 Genomics Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/ucal-berkeley.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/NakovSSH04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2004 Genomics Track Experiments at UTA: The Effects of Primary  Keys, Bigram Phrases and Query Expansion on Retrieval Performance

_Ari Pirkola_

- :fontawesome-solid-user-group: **Participant:** [u.tampere](./participants.md#u.tampere)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/utampere.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/utampere.geo.pdf)
- :material-file-search: **Runs:** [utaauto](./runs.md#utaauto) | [utamanu](./runs.md#utamanu)

??? abstract "Abstract"
	
	We submitted runs for Genomics Track's ad hoc retrieval task. The first official run (utaauto) was an automatic run and the second (utamanu) manual. For utaauto, the main features of query formulation were the removal of performative and marginally topical words from the topics based on average term frequency statistics, the removal of stop-words, the identification of bigram phrases, the weighting of keys with low document frequency (which we call primary keys), and query expansion with MH terms. The utamanu queries were Boolean queries formulated on a basis of a concept analysis. New terms were selected from the MeSH, genome databases, and dictionaries. The mean average precision (MAP) for the utaauto queries was 0.3324 and for the utamanu queries 0.3128. In the additional experiments we studied the effects of utaauto's main features on retrieval performance. The results showed that assigning more weight to the primary key than the other keys of a query improves retrieval performance. The use of bigram phrases in queries was also useful. The bigram phrases were identified using a collocation technique that computes an adjacency indicator for words in topics based on the joint occurrences of the words in a large and small window of document text words. We call the technique relative key adjacency (RKA).
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Pirkola04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Pirkola04,
		author = {Ari Pirkola},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2004 Genomics Track Experiments at {UTA:} The Effects of Primary Keys, Bigram Phrases and Query Expansion on Retrieval Performance},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/utampere.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Pirkola04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Report on the TREC 2004 Experiment: Genomics Track

_Patrick Ruch, Christine Chichester, Gilles Cohen, Frédéric Ehrler, Paul Fabry, Johan Marty, Henning Müller, Antoine Geissbühler_

- :fontawesome-solid-user-group: **Participant:** [u.hospital.geneva](./participants.md#u.hospital.geneva)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/uhosp-geneva.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/uhosp-geneva.geo.pdf)
- :material-file-search: **Runs:** [geneteam1](./runs.md#geneteam1) | [geneteam2](./runs.md#geneteam2) | [geneteam3](./runs.md#geneteam3) | [geneteamA1](./runs.md#geneteama1) | [geneteamA2](./runs.md#geneteama2) | [geneteamA3](./runs.md#geneteama3) | [geneteamA4](./runs.md#geneteama4) | [geneteamA5](./runs.md#geneteama5)

??? abstract "Abstract"
	
	Because of corruptions in the XML TREC Genomics collection, which were detected only some days before the submission deadline, we were not able to submit runs for the ad hoc retrieval task (task I), although relevance judgements made after polling were used to evaluate our approaches, and therefore this report mostly focuses on the text categorization task (task II: triage and annotation). Task I. Our approach uses thesaural resources (from the UMLS) together with a variant of the Porter stemmer for string normalization. Gene and Protein Entities (GPE) of the collection were simply marked up by dictionary look up during the indexing in order to avoid erroneous conflation: strings not found in the UMLS Specialist lexicon (augmented with various English lexical resources) were considered as GPE and were moderately overweighed. Two different weighting schemas were tested: first, a standard tf-idf with cosine normalization, second a weighting based on the deviation from randomness model. For indexing the Genomic collection, the following MEDLINE records were selected: article's titles, MeSH and RN terms, and abstract fields. We investigated the use of high-precisions strategies and our system returned only highly reliable documents so that some queries were not answered by the system. Our best run achieved an average precision of 32% (ranked 6 out of 27 participants). The score was obtained using UMLS resources and GPE (Gene and Protein Entity) tagging together with a combination of a classical atc.ltn schema (following SMART notation) with a deviation from randomness [8] weighting: L(n e)C2 and KL for expansion. Task II. We participated in both the triage and annotation tasks. For these tasks we attempted to adapt a Gene Ontology categorizer, which showed very effective results in the context of the BioCreative challenge, where training data were very sparse. The tool was completed by a naïve Bayes learner in order to take advantage of the TREC training data. The use of the last year GeneRIF extraction tool has also been evaluated.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RuchCCEFMMG04.bib) "
	```
	@inproceedings{DBLP:conf/trec/RuchCCEFMMG04,
		author = {Patrick Ruch and Christine Chichester and Gilles Cohen and Fr{\'{e}}d{\'{e}}ric Ehrler and Paul Fabry and Johan Marty and Henning M{\"{u}}ller and Antoine Geissb{\"{u}}hler},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Report on the {TREC} 2004 Experiment: Genomics Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/uhosp-geneva.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RuchCCEFMMG04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### UB at TREC 13: Genomics Track

_Miguel E. Ruiz, Munirathnam Srikanth, Rohini K. Srihari_

- :fontawesome-solid-user-group: **Participant:** [suny.buffalo](./participants.md#suny.buffalo)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/stateuny-buffalo.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/stateuny-buffalo.geo.pdf)
- :material-file-search: **Runs:** [UBgtNormJM1](./runs.md#ubgtnormjm1)

??? abstract "Abstract"
	
	This paper describes the experiments of the State University of New York at Buffalo in TREC 13. We participated in the Genomics track and submitted official runs to the Adhoc retrieval task. Our approach uses a language model IR system developed in house. We also present unofficial results for the triage sub-task of categorization task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/RuizSS04.bib) "
	```
	@inproceedings{DBLP:conf/trec/RuizSS04,
		author = {Miguel E. Ruiz and Munirathnam Srikanth and Rohini K. Srihari},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{UB} at {TREC} 13: Genomics Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/stateuny-buffalo.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/RuizSS04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC 2004 Genomics Track Experiments at IUB

_Kazuhiro Seki, James C. Costello, Vasanth R. Singan, Javed Mostafa_

- :fontawesome-solid-user-group: **Participant:** [indiana.u.seki](./participants.md#indiana.u.seki)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/indianau-seki.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/indianau-seki.geo.pdf)
- :material-file-search: **Runs:** [lga1](./runs.md#lga1) | [lga2](./runs.md#lga2) | [lgcab1](./runs.md#lgcab1) | [lgcab2](./runs.md#lgcab2) | [lgcad1](./runs.md#lgcad1) | [lgcad2](./runs.md#lgcad2) | [lgct1](./runs.md#lgct1) | [lgct2](./runs.md#lgct2)

??? abstract "Abstract"
	
	This paper describes the methods we developed for the three tasks of the TREC Genomics Track, i.e., ad hoc retrieval, triage, and annotation tasks. For the ad hoc retrieval task, we used the classic vector space model and studied the use of query expansion and pseudo-relevance feedback. Our submitted runs obtained a MAP of 0.183. For the triage task, we adopted a naive Bayes classifier trained on MeSH terms and used gene names as filters to rule out false positives. The obtained normalized utility score was 0.435. For the annotation task, we focused on document representation and applied a variant of the kNN classifiers. One of our submitted runs produced an F1 score of 0.561, ranking first out of 36 runs submitted for the annotation task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SekiCSM04.bib) "
	```
	@inproceedings{DBLP:conf/trec/SekiCSM04,
		author = {Kazuhiro Seki and James C. Costello and Vasanth R. Singan and Javed Mostafa},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} 2004 Genomics Track Experiments at {IUB}},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/indianau-seki.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SekiCSM04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Exploiting Zone Information, Syntactic Rules, and Informative Terms  in Gene Ontology Annotation of Biomedical Documents

_Burr Settles, Mark Craven_

- :fontawesome-solid-user-group: **Participant:** [u.wisconsin](./participants.md#u.wisconsin)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/uwisconsin.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/uwisconsin.geo.pdf)
- :material-file-search: **Runs:** [wiscWRT](./runs.md#wiscwrt) | [wiscW](./runs.md#wiscw) | [wiscWR](./runs.md#wiscwr) | [wiscWT](./runs.md#wiscwt)

??? abstract "Abstract"
	
	We describe a system developed for the Annotation Hierarchy subtask of the Text Retrieval Conference (TREC) 2004 Genomics Track. The goal of this track is to automatically predict Gene Ontology (GO) domain annotations given full-text biomedical journal articles and associated genes. Our system uses a two-tier statistical machine learning system that makes predictions first on 'zone'-level text (i.e. abstract, introduction, etc.) and then combines evidence to make final document-level predictions. We also describe the effects of more advanced syntactic features (equivalence classes of syntactic patterns) and 'informative terms' (phrases semantically linked to specific GO codes). These features are induced automatically from the training data and external sources, such as 'weakly labeled' MED-LINE abstracts. Our baseline system (using only traditional word features), significantly exceeds median F1 of all task submissions on unseen test data. We show further improvement by including syntactic features and informative term features. Our complete system exceeds median performance for all three evaluation metrics (precision, recall, and F1), and achieves the second highest reported F1 of all systems in the track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SettlesC04.bib) "
	```
	@inproceedings{DBLP:conf/trec/SettlesC04,
		author = {Burr Settles and Mark Craven},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Exploiting Zone Information, Syntactic Rules, and Informative Terms in Gene Ontology Annotation of Biomedical Documents},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/uwisconsin.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SettlesC04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### TREC Genomics 2004

_Gail Sinclair, Bonnie L. Webber_

- :fontawesome-solid-user-group: **Participant:** [u.edinburgh.sinclair](./participants.md#u.edinburgh.sinclair)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/uedinburgh-sinclair.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/uedinburgh-sinclair.geo.pdf)
- :material-file-search: **Runs:** [edinauto2](./runs.md#edinauto2) | [edinauto5](./runs.md#edinauto5) | [epub2](./runs.md#epub2) | [eint2](./runs.md#eint2) | [emet2](./runs.md#emet2) | [eres2](./runs.md#eres2) | [edis2](./runs.md#edis2)

??? abstract "Abstract"
	
	The TREC Genomics track started in 2003 as the first domain specific track of the Text Retrieval Competition. The aim of the track is to develop various IR tasks specific to the biomedical field. One task of the first year involved the retrieval of documents given a specific gene, while the second task required the extraction a brief description of gene function from documents. This year sees a foray into ad hoc retrieval and a curation and categorization task.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/SinclairW04.bib) "
	```
	@inproceedings{DBLP:conf/trec/SinclairW04,
		author = {Gail Sinclair and Bonnie L. Webber},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{TREC} Genomics 2004},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/uedinburgh-sinclair.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/SinclairW04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Meiji University Web, Novelty and Genomic Track Experiments

_Tomoe Tomiyama, Kosuke Karoji, Takeshi Kondo, Yuichi Kakuta, Tomohiro Takagi_

- :fontawesome-solid-user-group: **Participant:** [meiji.u](./participants.md#meiji.u)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/meijiu.web.novelty.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/meijiu.web.novelty.geo.pdf)
- :material-file-search: **Runs:** [MeijiHilG](./runs.md#meijihilg)

??? abstract "Abstract"
	
	We participated in Novelty track, the topic distillation task of Web track and ad hoc task of Genomic Track. Our main challenge is to deal with meaning of words and improve retrieval performance.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/TomiyamaKKKT04.bib) "
	```
	@inproceedings{DBLP:conf/trec/TomiyamaKKKT04,
		author = {Tomoe Tomiyama and Kosuke Karoji and Takeshi Kondo and Yuichi Kakuta and Tomohiro Takagi},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Meiji University Web, Novelty and Genomic Track Experiments},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/meijiu.web.novelty.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/TomiyamaKKKT04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Information Needs and Automatic Queries

_Richard M. Tong_

- :fontawesome-solid-user-group: **Participant:** [tarragon](./participants.md#tarragon)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/tarragon.tong.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/tarragon.tong.geo.pdf)
- :material-file-search: **Runs:** [tgnSplit](./runs.md#tgnsplit) | [tgnNecaux](./runs.md#tgnnecaux)

??? abstract "Abstract"
	
	Tarragon Consulting Corporation participated in the adhoc retrieval task of the TREC 2004 Genomics Track. We used a standard deployment of the K2 search engine from Verity, Inc. in which we exploited the free-text query parser to interpret the information need statements provided in the task. The primary goal of our participation was to establish a performance baseline using “of-the-shelf” tools and then to explore how knowledge-based extensions could enhance performance. Time and resource constraints prevented us from performing the knowledge-based experiments, but our official submissions show that reasonable performance can be achieved using just our baseline strategy.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/Tong04.bib) "
	```
	@inproceedings{DBLP:conf/trec/Tong04,
		author = {Richard M. Tong},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Information Needs and Automatic Queries},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/tarragon.tong.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/Tong04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### WIDIT in TREC 2004 Genomics, Hard, Robust and Web Tracks

_Kiduk Yang, Ning Yu, Adam Wead, Gavin La Rowe, Yu-Hsiu Li, Christopher Friend, Yoon Lee_

- :fontawesome-solid-user-group: **Participant:** [indiana.u.yang](./participants.md#indiana.u.yang)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/indianau.geo.hard.robust.web.pdf](http://trec.nist.gov/pubs/trec13/papers/indianau.geo.hard.robust.web.pdf)
- :material-file-search: **Runs:** [wdvqlxa1](./runs.md#wdvqlxa1) | [wdvqlx1](./runs.md#wdvqlx1) | [wdtriage1](./runs.md#wdtriage1)

??? abstract "Abstract"
	
	To facilitate understanding of information as well as its discovery, we need to combine the capabilities of the human and the machine as well as multiple methods and sources of evidence. Web Information Discovery Tool (WIDIT) Laboratory at the Indiana University School of Library and Information Science houses several projects that aim to apply this idea of multi-level fusion in the areas of information retrieval and knowledge organization. The TREC research group of WIDIT, who engages in examination of information retrieval strategies that can accommodate a variety of data environments and search tasks, participated in the Genomics, HARD, Robust, and Web tracks in TREC-2004. The basic approach of WIDIT was to leverage multiple sources of evidence, combine multiple methods, and integrate the strengths of man and the machine. Our main strategies for the tracks were: the use of gene name thesaurus in the Genomics track; query expansion and relevance feedback in the HARD track; query expansion with keywords from Web search in the Robust track, and the interactive system tuning process called “Dynamic Tuning” in the Web track.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/YangYWRLFL04.bib) "
	```
	@inproceedings{DBLP:conf/trec/YangYWRLFL04,
		author = {Kiduk Yang and Ning Yu and Adam Wead and Gavin La Rowe and Yu{-}Hsiu Li and Christopher Friend and Yoon Lee},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {{WIDIT} in {TREC} 2004 Genomics, Hard, Robust and Web Tracks},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/indianau.geo.hard.robust.web.pdf},
		timestamp = {Tue, 24 Nov 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/YangYWRLFL04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

#### Experience of Using SVM for the Triage Task in TREC 2004 Genomics  Track

_Dell Zhang, Wee Sun Lee_

- :fontawesome-solid-user-group: **Participant:** [mlg.nus](./participants.md#mlg.nus)
- :material-file-pdf-box: **Paper:** [http://trec.nist.gov/pubs/trec13/papers/natusing.zhang.geo.pdf](http://trec.nist.gov/pubs/trec13/papers/natusing.zhang.geo.pdf)
- :material-file-search: **Runs:** [nusbird2004a](./runs.md#nusbird2004a) | [nusbird2004b](./runs.md#nusbird2004b) | [nusbird2004c](./runs.md#nusbird2004c) | [nusbird2004d](./runs.md#nusbird2004d) | [nusbird2004e](./runs.md#nusbird2004e)

??? abstract "Abstract"
	
	This paper reports our knowledge-ignorant machine learning approach to the triage task in TREC2004 genomics track, which is actually a text categorization problem. We applied Support Vector Machine (SVM) and found that information-gain based feature selection is helpful. Although we achieved decent performance in leave-one-out cross-validation experiments, the evaluation result on the test data turned out to be surprisingly poor. Further experiments revealed that there is a chasm between the training and test data distributions. It seems that more aggressive feature selection can partially alleviate the trouble caused by distribution change.
	

??? quote "Bibtex [:material-link-variant:](https://dblp.org/rec/conf/trec/ZhangL04.bib) "
	```
	@inproceedings{DBLP:conf/trec/ZhangL04,
		author = {Dell Zhang and Wee Sun Lee},
		editor = {Ellen M. Voorhees and Lori P. Buckland},
		title = {Experience of Using {SVM} for the Triage Task in {TREC} 2004 Genomics Track},
		booktitle = {Proceedings of the Thirteenth Text REtrieval Conference, {TREC} 2004, Gaithersburg, Maryland, USA, November 16-19, 2004},
		series = {{NIST} Special Publication},
		volume = {500-261},
		publisher = {National Institute of Standards and Technology {(NIST)}},
		year = {2004},
		url = {http://trec.nist.gov/pubs/trec13/papers/natusing.zhang.geo.pdf},
		timestamp = {Thu, 12 Mar 2020 00:00:00 +0100},
		biburl = {https://dblp.org/rec/conf/trec/ZhangL04.bib},
		bibsource = {dblp computer science bibliography, https://dblp.org}
	}
	```

